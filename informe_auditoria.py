#!/usr/bin/env python3
import sys

def generar_informe_auditoria():
    print("[*] Iniciando escaneo y auditoría CIS Benchmark (Modo Local)...")

    # Hallazgos simulados de la auditoría inicial (previo al hardening)
    informe_previo = [
        "[CIS-01] [NO CUMPLE] Las contraseñas no están encriptadas globalmente.",
        "[CIS-02] [NO CUMPLE] Falta configurar el tiempo de inactividad (exec-timeout) en VTY.",
        "[CIS-03] [NO CUMPLE] No se encontró un banner de advertencia (banner motd).",
        "[CIS-04] [NO CUMPLE] El servidor HTTP web está activo o no deshabilitado explícitamente.",
        "[CIS-05] [NO CUMPLE] No se ha forzado el uso exclusivo de SSH versión 2."
    ]

    print("\n--- INFORME DE AUDITORÍA INICIAL (PREVIO AL HARDENING) ---")
    for linea in informe_previo:
        print(linea)

    # Guardar informe previo en archivo
    with open("informe_auditoria.txt", "w") as f:
        f.write("=== INFORME DE AUDITORIA CIS (PREVIO) ===\n")
        f.write("\n".join(informe_previo) + "\n")

    # Interacción simulada para aplicar el hardening
    opcion = input("\n¿Desea aplicar las reglas de Hardening automáticamente en el equipo? (s/n): ").strip().lower()

    if opcion == 's':
        print("\n[*] Aplicando configuración de Hardening basada en CIS...")
        print("[+] Reglas de Hardening aplicadas y guardadas correctamente en la NVRAM.")

        # Hallazgos tras aplicar el hardening (póstumo)
        informe_post = [
            "[CIS-01] [CUMPLE] Encriptación de contraseñas activada (service password-encryption).",
            "[CIS-02] [CUMPLE] Tiempo de inactividad configurado en líneas VTY.",
            "[CIS-03] [CUMPLE] Banner de advertencia legal configurado correctamente.",
            "[CIS-04] [CUMPLE] Servidor HTTP web deshabilitado por seguridad.",
            "[CIS-05] [CUMPLE] Protocolo SSH versión 2 forzado."
        ]

        print("\n--- INFORME DE AUDITORÍA PÓSTUMO (TRAS EL HARDENING) ---")
        for linea in informe_post:
            print(linea)

        # Agregar informe póstumo al archivo
        with open("informe_auditoria.txt", "a") as f:
            f.write("\n=== INFORME DE AUDITORIA CIS (POST-HARDENING) ===\n")
            f.write("\n".join(informe_post) + "\n")

        print("\n[+] Proceso finalizado con éxito. Reporte completo guardado en: informe_auditoria.txt")
    else:
        print("\n[*] Proceso finalizado sin aplicar modificaciones. Solo se generó el reporte inicial.")

if __name__ == "__main__":
    generar_informe_auditoria()