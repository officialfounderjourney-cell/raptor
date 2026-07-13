from django.conf import settings
from django.core.files.base import File
from django.core.files.storage import Storage
from vercel.blob import BlobClient
import io
import os


class VercelBlobMediaStorage(Storage):
    def __init__(self):
        self.client = BlobClient()
        self.base_path = settings.MEDIAFILES_LOCATION

    def _full_path(self, name):
        return f"{self.base_path}/{name}"

    def _save(self, name, content):
        path = self._full_path(name)
        if content.multiple_chunks():
            content.seek(0)
            self.client.put(path, content.read(), access="public")
        else:
            content.seek(0)
            self.client.put(path, content.read(), access="public")
        return name

    def _open(self, name, mode="rb"):
        path = self._full_path(name)
        blob = self.client.get(path)
        return File(io.BytesIO(blob), name)

    def url(self, name):
        path = self._full_path(name)
        try:
            meta = self.client.head(path)
            return meta.url
        except Exception:
            return ""

    def delete(self, name):
        path = self._full_path(name)
        try:
            meta = self.client.head(path)
            self.client.delete([meta.url])
        except Exception:
            pass

    def exists(self, name):
        path = self._full_path(name)
        try:
            self.client.head(path)
            return True
        except Exception:
            return False

    def size(self, name):
        path = self._full_path(name)
        try:
            meta = self.client.head(path)
            return meta.size
        except Exception:
            return 0
