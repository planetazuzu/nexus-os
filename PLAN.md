# NEXUS OS Dashboard - Plan de Implementación

## Estado
- **Desarrollador:** FORGE (G1) — offline, esperar reconexión
- **Ubicación:** /var/www/nexus-os/
- **Puerto:** 3333
- **Token:** nexus-secret-2026

## Stack
- Frontend: HTML + CSS + Vanilla JS (mobile-first)
- Backend: FastAPI (Python)
- Base de datos: PostgreSQL (blackbox-postgres-1)
- Autenticación: Token header

## Requisitos
- ✅ Mobile-first responsive
- ✅ Autenticación obligatoria
- ✅ 12 módulos navegables
- ✅ Conexión a agentes via API

## Módulos Fase 1
1. Command Center - KPIs, log, chat
2. Agentes - Estado BLACKBOX/FORGE/CLAWMARK
3. Tareas - CRUD básico

## Módulos Fase 2
4. Costes y ROI
5. Proyectos e Ideas
6. Comunicaciones

## Módulos Fase 3
7. Documentación
8. Agenda
9. Automatizaciones
10. Recursos
11. Finanzas
12. Salud

## Pasos para FORGE
1. Crear estructura carpetas
2. Implementar backend FastAPI con auth
3. Crear frontend mobile-first con CSS proporcionado
4. Dockerizar y desplegar en puerto 3333

## Comandos
```bash
cd /var/www/nexus-os
docker build -t nexus-os .
docker run -d -p 3333:3333 --name nexus-dashboard \
  -e NEXUS_TOKEN=nexus-secret-2026 \
  -e DATABASE_URL=postgresql://blackbox:blackbox123@blackbox-postgres-1:5432/nexus \
  nexus-os
```
