# Project Bible - README

## Propósito

Bienvenido al **Project Bible** del proyecto de eCommerce de bicicletas.

Este repositorio representa la única fuente oficial de verdad (Single Source of Truth) para el proyecto. Antes de escribir código, modificar una funcionalidad o solicitar trabajo a un agente de IA, la respuesta debe existir aquí.

## Contexto

- El proyecto **no es una migración** desde otra plataforma.
- Existe un competidor en Shopify que se utilizará únicamente como **benchmark**.
- Se desarrollará una plataforma propia sobre **CycleBay** con control total del código, infraestructura y evolución.
- El objetivo del MVP es vender productos reales de principio a fin, no superar al benchmark desde el día uno.

## Base Tecnológica: CycleBay

**Actualización Técnica Fundamental**

Tras una evaluación exhaustiva, se ha decidido que la base tecnológica del proyecto será **CycleBay** en lugar de EverShop.

### ¿Por qué CycleBay?

- Es un proyecto open-source (Django) específicamente diseñado para un eCommerce B2C de bicicletas.
- Su modelo de datos y lógica de negocio (gestión de tallas, stock, colores) se alinea perfectamente con nuestros requisitos.
- Proporciona una base funcional completa (catálogo, carrito, checkout con Stripe, panel de administración) que acelera drásticamente el desarrollo del MVP.
- Nos permite seguir la filosofía de "definir antes de programar", pero partiendo de una base probada, enfocando nuestros esfuerzos en la personalización y las funcionalidades diferenciales.

### Agradecimiento

Este proyecto se basa en el excelente trabajo de **Pavlo Myskov** y su proyecto **CycleBay**. Queremos expresar nuestro más sincero agradecimiento por compartir su código como open-source y proporcionar una base tan sólida y bien documentada para nuestra plataforma.

- **Repositorio original:** https://github.com/pavlo-myskov/cyclebay
- **Demo en vivo:** https://cyclebay-bc1e75ddbf8e.herokuapp.com/

## Filosofía

1. Definir antes de programar.
2. El MVP tiene prioridad sobre las ideas.
3. Extender CycleBay sin modificar su lógica core.
4. Toda decisión importante queda documentada.
5. La IA acelera el desarrollo, pero no reemplaza una buena especificación.

## Estructura del Project Bible

```text
/docs
│
├── README.md
├── 00_Project_Charter.md
├── 01_Product_Vision.md
├── 02_Business_Discovery.md
├── 03_MVP_Specification.md
├── 04_Technical_Architecture.md
├── 05_Database_Planning.md
├── 06_UX_Design_System.md
├── 07_SEO_Content_Strategy.md
├── 08_AI_Development_Rules.md
├── 09_Roadmap.md
├── 10_Decision_Log.md
├── 11_Definition_of_Done.md
├── 12_Go_Live_Checklist.md
└── appendix/
    ├── Benchmark.md
    ├── Business_Rules.md
    ├── Glossary.md
    ├── Prompt_Library.md
    ├── API_Inventory.md
    ├── Environment_Variables.md
    └── Tech_Stack.md
