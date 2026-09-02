---
product: Gelaxiz Status
platform: web
authority: inferred from the existing Upptime configuration and Gelaxiz main-site design documentation
---

# Product

Gelaxiz Status is the public operational view for the Gelaxiz ecosystem. It gives Niilo, friends, and visitors a fast, honest answer to one question: are the services working right now?

## Users and context

- Visitors checking whether a Gelaxiz service is available before troubleshooting locally.
- The operator scanning current incidents, individual service health, and recent response-time history.
- Desktop and mobile use, often during an outage when speed and clarity matter more than decoration.

## Core experience

The first viewport establishes the system identity, explains that checks are live, and makes current incidents and service state immediately scannable. Each service remains linked to its generated history page. Time-range controls, incident reports, scheduled maintenance, and Upptime's generated data remain fully functional.

## Constraints

- Preserve Upptime's generated markup, GitHub-backed monitoring, incident workflow, and all configured services.
- Never imply that a service is healthy without data from Upptime.
- Keep state understandable without relying on color alone.
- Keep controls at least 44 px tall on touch layouts.
- Respect `prefers-reduced-motion`.
- Maintain the shared Gelaxiz minimal-dark ecosystem rather than introducing a separate brand.

