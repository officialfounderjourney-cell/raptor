import io
import os
import requests

from django.conf import settings
from django.core.files.base import File
from django.core.files.storage import Storage


BLOB_API = "https://blob.vercel-storage.com"


def _get_token():
    return os.environ.get("BLOB_READ_WRITE_TOKEN", "")


class VercelBlobMediaStorage(Storage):
    def __init__(self):
        self.base_path = settings.MEDIAFILES_LOCATION
        self._url_cache = {}

    def _full_path(self, name):
        return f"{self.base_path}/{name}"

    def _headers(self):
        token = _get_token()
        if not token:
            return {}
        return {"Authorization": f"Bearer {token}"}

    def _save(self, name, content):
        path = self._full_path(name)
        content.seek(0)
        data = content.read()

        resp = requests.put(
            f"{BLOB_API}/upload",
            params={"pathname": path},
            headers=self._headers(),
            data=data,
        )
        resp.raise_for_status()
        result = resp.json()
        self._url_cache[path] = result["url"]
        return name

    def _open(self, name, mode="rb"):
        url = self.url(name)
        if not url:
            raise FileNotFoundError(f"No blob found for {name}")
        resp = requests.get(url)
        resp.raise_for_status()
        return File(io.BytesIO(resp.content), name)

    def url(self, name):
        path = self._full_path(name)
        if path in self._url_cache:
            return self._url_cache[path]

        resp = requests.get(
            f"{BLOB_API}/",
            params={"prefix": path, "limit": 1},
            headers=self._headers(),
        )
        if resp.ok:
            data = resp.json()
            blobs = data.get("blobs", [])
            if blobs:
                self._url_cache[path] = blobs[0]["url"]
                return blobs[0]["url"]
        return ""

    def delete(self, name):
        path = self._full_path(name)
        url = self._url_cache.pop(path, None)
        if not url:
            resp = requests.get(
                f"{BLOB_API}/",
                params={"prefix": path, "limit": 1},
                headers=self._headers(),
            )
            if resp.ok:
                data = resp.json()
                blobs = data.get("blobs", [])
                if blobs:
                    url = blobs[0]["url"]
        if url:
            requests.post(
                f"{BLOB_API}/delete",
                headers=self._headers(),
                json={"urls": [url]},
            )

    def exists(self, name):
        path = self._full_path(name)
        resp = requests.get(
            f"{BLOB_API}/",
            params={"prefix": path, "limit": 1},
            headers=self._headers(),
        )
        if resp.ok:
            data = resp.json()
            return len(data.get("blobs", [])) > 0
        return False

    def size(self, name):
        path = self._full_path(name)
        resp = requests.get(
            f"{BLOB_API}/",
            params={"prefix": path, "limit": 1},
            headers=self._headers(),
        )
        if resp.ok:
            data = resp.json()
            blobs = data.get("blobs", [])
            if blobs:
                return blobs[0]["size"]
        return 0
