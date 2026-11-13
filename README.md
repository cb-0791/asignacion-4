# Asignación 4: Hardening de Redes y Auditoría CIS (FortiGate y Cisco)

video:
---

##  1. Propósito del Laboratorio
El objetivo de este proyecto es implementar una topología de red segura e integrada que conecta una máquina cliente (Ubuntu), un Firewall de perímetro (FortiGate-0791) y un Router de núcleo (Cisco-0791). Sobre esta infraestructura, se ejecuta una auditoría de seguridad automatizada basada en los estándares del **CIS Benchmark**, seguida de la aplicación de políticas de *hardening* (endurecimiento) para mitigar vulnerabilidades y garantizar la resiliencia operativa de la red ante accesos no autorizados.

---

##  2. Topología de Red y Direccionamiento
La red ha sido diseñada bajo el esquema de direccionamiento basado en la matrícula institucional:
* **Cliente de Seguridad (Ubuntu):** `10.7.91.203` (Subred LAN `10.7.91.128/25`)
* **Firewall Perimetral (FortiGate-0791):**
  * `port1` (WAN / Enlace P2P): `10.255.255.2 /30`
  * `port2` (LAN / Puerta de enlace): `10.7.91.130 /25`
* **Router de Núcleo (Router-Cisco-0791):**
  * `GigabitEthernet0/0`: `10.255.255.1 /30`

### 📊 Diagrama de Topología
[ Ubuntu (10.7.91.203) ]
│ (10.7.91.130)
▼
[ FortiGate-0791 ] ──(P2P 10.255.255.0/30)── [ Router-Cisco-0791 (10.255.255.1) ]

> **Evidencia visual:** <img width="326" height="411" alt="imagen_2026-11-13_184900607" src="https://github.com/user-attachments/assets/04f5466f-5277-4481-bc68-334e4ef03b61" />

---

## 🔍 3. Análisis de Seguridad basado en CIS Benchmark
El script automatizado evalúa las siguientes directrices críticas de seguridad en los equipos de red:
1. **Encriptación de Contraseñas (`service password-encryption`):** Evita la exposición de credenciales en texto plano dentro de la configuración activa.
2. **Control de Inactividad en Consolas VTY (`exec-timeout`):** Cierra de manera automática sesiones remotas inactivas para prevenir ataques de secuestro de sesión.
3. **Banner de Advertencia Legal (`banner motd`):** Establece una advertencia disuasoria y explícita para fundamentar el marco legal ante accesos no autorizados.

---

## 🛠️ 4. Evidencias de Ejecución y Pruebas
### Auditoría Previa (Sin Hardening)
Al ejecutar el script por primera vez, se detectan las deficiencias normativas generando el reporte inicial:
<img width="961" height="500" alt="image" src="https://github.com/user-attachments/assets/a1604890-88e0-48b3-a76d-a53d1a357c9f" />

<img width="1032" height="143" alt="image" src="https://github.com/user-attachments/assets/054e8522-2cf7-4487-9ca2-b9977be622b0" />


### Aplicación de Hardening y Verificación Póstuma
Tras aplicar las políticas recomendadas por el estándar CIS, las pruebas de verificación confirman la correcta mitigación de los riesgos:
<img width="1025" height="123" alt="image" src="https://github.com/user-attachments/assets/4a45c92b-2ad7-4b68-aa25-8377bda6cb10" />


---
