# Real Estate Platform

A platform for both end users (clients) and real estate agencies to search for properties (houses, apartments, studio apartments, single rooms and garages) within a chosen radius, in kilometers, from a given starting point. The system shows every property inside that radius and lets users narrow the results with more specific filters that match what they are looking for.

Once a client selects one or more properties, they can see each property's full details: photos, descriptions and directions to get there. They can also contact a real estate agent to schedule a visit or get advice.

The goal is to provide an all-in-one platform for managing properties, and for finding and offering them as quickly as possible, according to each client's criteria and preferences.

## Features (version 1)

- Publish properties with photos
- Search by radius on a map, from any starting point
- Filter results by price and property type
- AI-generated property descriptions
- Search written in natural language, understood by AI

## Tech stack

| Layer          | Technology                                         |
| -------------- | -------------------------------------------------- |
| Frontend       | React with Vite, and Leaflet for the map           |
| Backend        | Python with FastAPI                                |
| Database       | PostgreSQL with PostGIS for geographic queries     |
| Containers     | Docker and Docker Compose                          |
| CI/CD          | GitHub Actions                                     |
| Infrastructure | Ansible and Terraform, deployed on Proxmox and AWS |
| Monitoring     | Prometheus and Grafana                             |

## Roadmap

- A built-in CRM to manage clients
- Role-based access: administrator, real estate supervisor, real estate agent, property owner and end client, each with their own permissions
- Contact with an agent to schedule visits or get advice
- Voice search, AI agents, a statistics dashboard and a mobile app
