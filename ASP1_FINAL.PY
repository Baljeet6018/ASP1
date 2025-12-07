import numpy as np
import matplotlib.pyplot as plt
def importar_datos():
    # ============================================
    # BUS DATA - Datos de Datos.txt (mpc.bus)
    # ============================================
    # Bus type: 3=Slack, 2=PV, 1=PQ (notación estándar mantenida)
    # Columns: Bus, Type, Pd, Qd, Gs, Bs, area, Vm, Va, baseKV, zone, Vmax, Vmin
    busdata_raw = np.array([
        [1,  3, 0,     0,    0,  0,   1, 1.06,  0,      132, 1, 1.06, 0.94],
        [2,  2, 21.7,  12.7, 0,  0,   1, 1.043, -5.48,  132, 1, 1.06, 0.94],
        [3,  1, 2.4,   1.2,  0,  0,   1, 1.021, -7.96,  132, 1, 1.06, 0.94],
        [4,  1, 7.6,   1.6,  0,  0,   1, 1.012, -9.62,  132, 1, 1.06, 0.94],
        [5,  2, 94.2,  19,   0,  0,   1, 1.01,  -14.37, 132, 1, 1.06, 0.94],
        [6,  1, 0,     0,    0,  0,   1, 1.01,  -11.34, 132, 1, 1.06, 0.94],
        [7,  1, 22.8,  10.9, 0,  0,   1, 1.002, -13.12, 132, 1, 1.06, 0.94],
        [8,  2, 30,    30,   0,  0,   1, 1.01,  -12.1,  132, 1, 1.06, 0.94],
        [9,  1, 0,     0,    0,  0,   1, 1.051, -14.38, 1,   1, 1.06, 0.94],
        [10, 1, 5.8,   2,    0,  19,  1, 1.045, -15.97, 33,  1, 1.06, 0.94],
        [11, 2, 0,     0,    0,  0,   1, 1.082, -14.39, 11,  1, 1.06, 0.94],
        [12, 1, 11.2,  7.5,  0,  0,   1, 1.057, -15.24, 33,  1, 1.06, 0.94],
        [13, 2, 0,     0,    0,  0,   1, 1.071, -15.24, 11,  1, 1.06, 0.94],
        [14, 1, 6.2,   1.6,  0,  0,   1, 1.042, -16.13, 33,  1, 1.06, 0.94],
        [15, 1, 8.2,   2.5,  0,  0,   1, 1.038, -16.22, 33,  1, 1.06, 0.94],
        [16, 1, 3.5,   1.8,  0,  0,   1, 1.045, -15.83, 33,  1, 1.06, 0.94],
        [17, 1, 9,     5.8,  0,  0,   1, 1.04,  -16.14, 33,  1, 1.06, 0.94],
        [18, 1, 3.2,   0.9,  0,  0,   1, 1.028, -16.82, 33,  1, 1.06, 0.94],
        [19, 1, 9.5,   3.4,  0,  0,   1, 1.026, -17,    33,  1, 1.06, 0.94],
        [20, 1, 2.2,   0.7,  0,  0,   1, 1.03,  -16.8,  33,  1, 1.06, 0.94],
        [21, 1, 17.5,  11.2, 0,  0,   1, 1.033, -16.42, 33,  1, 1.06, 0.94],
        [22, 1, 0,     0,    0,  0,   1, 1.033, -16.41, 33,  1, 1.06, 0.94],
        [23, 1, 3.2,   1.6,  0,  0,   1, 1.027, -16.61, 33,  1, 1.06, 0.94],
        [24, 1, 8.7,   6.7,  0,  4.3, 1, 1.021, -16.78, 33,  1, 1.06, 0.94],
        [25, 1, 0,     0,    0,  0,   1, 1.017, -16.35, 33,  1, 1.06, 0.94],
        [26, 1, 3.5,   2.3,  0,  0,   1, 1,     -16.77, 33,  1, 1.06, 0.94],
        [27, 1, 0,     0,    0,  0,   1, 1.023, -15.82, 33,  1, 1.06, 0.94],
        [28, 1, 0,     0,    0,  0,   1, 1.007, -11.97, 132, 1, 1.06, 0.94],
        [29, 1, 2.4,   0.9,  0,  0,   1, 1.003, -17.06, 33,  1, 1.06, 0.94],
        [30, 1, 10.6,  1.9,  0,  0,   1, 0.992, -17.94, 33,  1, 1.06, 0.94]
    ])

    # Generator data de Datos.txt (mpc.gen)
    # Columns: bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin...
    gen_data_raw = np.array([
        [1,  260.2, -16.1, 10,  0,   1.06,  100, 1],
        [2,  40,    50,    50,  -40, 1.045, 100, 1],
        [5,  0,     37,    40,  -40, 1.01,  100, 1],
        [8,  0,     37.3,  40,  -10, 1.01,  100, 1],
        [11, 0,     16.2,  24,  -6,  1.082, 100, 1],
        [13, 0,     10.6,  24,  -6,  1.071, 100, 1]
    ])
    busdata = busdata_raw.copy()
    # 3=Slack, 2=PV, 1=PQ (como viene originalmente)

    # ============================================
    # LINE DATA - Datos de Datos.txt (mpc.branch)
    # ============================================
    # El valor en Datos.txt YA es b_total, se dividirá al construir Ybus
    linedata = np.array([
        [1,  2,  0.0192, 0.0575, 0.0528, 1],      # ← SIN /2
        [1,  3,  0.0452, 0.1652, 0.0408, 1],
        [2,  4,  0.057,  0.1737, 0.0368, 1],
        [3,  4,  0.0132, 0.0379, 0.0084, 1],
        [2,  5,  0.0472, 0.1983, 0.0418, 1],
        [2,  6,  0.0581, 0.1763, 0.0374, 1],
        [4,  6,  0.0119, 0.0414, 0.009,  1],
        [5,  7,  0.046,  0.116,  0.0204, 1],
        [6,  7,  0.0267, 0.082,  0.017,  1],
        [6,  8,  0.012,  0.042,  0.009,  1],
        [6,  9,  0.0,    0.208,  0.0,    0.978],
        [6,  10, 0.0,    0.556,  0.0,    0.969],
        [9,  11, 0.0,    0.208,  0.0,    1],
        [9,  10, 0.0,    0.11,   0.0,    1],
        [4,  12, 0.0,    0.256,  0.0,    0.932],
        [12, 13, 0.0,    0.14,   0.0,    1],
        [12, 14, 0.1231, 0.2559, 0.0,    1],
        [12, 15, 0.0662, 0.1304, 0.0,    1],
        [12, 16, 0.0945, 0.1987, 0.0,    1],
        [14, 15, 0.221,  0.1997, 0.0,    1],
        [16, 17, 0.0524, 0.1923, 0.0,    1],
        [15, 18, 0.1073, 0.2185, 0.0,    1],
        [18, 19, 0.0639, 0.1292, 0.0,    1],
        [19, 20, 0.034,  0.068,  0.0,    1],
        [10, 20, 0.0936, 0.209,  0.0,    1],
        [10, 17, 0.0324, 0.0845, 0.0,    1],
        [10, 21, 0.0348, 0.0749, 0.0,    1],
        [10, 22, 0.0727, 0.1499, 0.0,    1],
        [21, 22, 0.0116, 0.0236, 0.0,    1],
        [15, 23, 0.1,    0.202,  0.0,    1],
        [22, 24, 0.115,  0.179,  0.0,    1],
        [23, 24, 0.132,  0.27,   0.0,    1],
        [24, 25, 0.1885, 0.3292, 0.0,    1],
        [25, 26, 0.2544, 0.38,   0.0,    1],
        [25, 27, 0.1093, 0.2087, 0.0,    1],
        [28, 27, 0.0,    0.396,  0.0,    0.968],
        [27, 29, 0.2198, 0.4153, 0.0,    1],
        [27, 30, 0.3202, 0.6027, 0.0,    1],
        [29, 30, 0.2399, 0.4533, 0.0,    1],
        [8,  28, 0.0636, 0.2,    0.0428, 1],
        [6,  28, 0.0169, 0.0599, 0.013,  1]
    ])
    return busdata, gen_data_raw, linedata
def construir_Ybus(linedata, busdata,No_of_Bus,BMva):
    # ============================================
    # EXTRACT LINE DATA
    # ============================================
    fb = linedata[:, 0].astype(int)
    tb = linedata[:, 1].astype(int)
    r = linedata[:, 2]
    x = linedata[:, 3]
    b_total = linedata[:, 4] 
    a = linedata[:, 5]

    z = r + 1j * x
    y = 1.0 / z

    nl = len(fb)
    No_of_Bus = max(np.max(fb), np.max(tb))

    # ============================================
    # FORMATION OF YBUS MATRIX
    # ============================================
    Y = np.zeros((No_of_Bus, No_of_Bus), dtype=complex)

    for k in range(nl):
        i = fb[k] - 1  # from bus
        j = tb[k] - 1  # to bus
        b_half = 1j * b_total[k] / 2.0
        Y[i, j] = Y[i, j] - y[k] / a[k]
        Y[j, i] = Y[j, i] - y[k] / a[k]  # ← NO asumir Y[j,i] = Y[i,j]
        Y[i, i] = Y[i, i] + (y[k] / (a[k]**2)) + b_half
        Y[j, j] = Y[j, j] + y[k] + b_half

    # Agregar shunt de los buses (Gs y Bs)
    BMva = 100
    for i in range(No_of_Bus):
        Gs = busdata[i, 4] / BMva
        Bs = busdata[i, 5] / BMva
        Y[i, i] = Y[i, i] + (Gs + 1j * Bs)

    return Y
def calcular_potencias(V, delta, G, B, No_of_Bus):
    P = np.zeros(No_of_Bus)
    Q = np.zeros(No_of_Bus)

    for i in range(No_of_Bus):
        for j in range(No_of_Bus):
            P[i] += V[i] * V[j] * (G[i, j] * np.cos(delta[i] - delta[j]) +
                                    B[i, j] * np.sin(delta[i] - delta[j]))
            Q[i] += V[i] * V[j] * (G[i, j] * np.sin(delta[i] - delta[j]) -
                                    B[i, j] * np.cos(delta[i] - delta[j]))
    return P, Q
def construir_Jacobiano(V, delta, G, B, P, No_of_Bus, PQ_Bus):
    No_of_PQ_Bus = len(PQ_Bus)
    # J1 (dP/dTheta)
    J1 = np.zeros((No_of_Bus - 1, No_of_Bus - 1))
    for i in range(No_of_Bus - 1):
        m = i + 1  # Índice real del bus (excluyendo Slack)
        for j in range(No_of_Bus - 1):
            n = j + 1
            if m == n:
                # Elemento diagonal
                for k in range(No_of_Bus):
                    J1[i, j] += V[m] * V[k] * (-G[m, k] * np.sin(delta[m] - delta[k]) +
                                                B[m, k] * np.cos(delta[m] - delta[k]))
                J1[i, j] = J1[i, j] - V[m]**2 * B[m, m]
            else:
                # Elemento fuera de diagonal
                J1[i, j] = V[m] * V[n] * (G[m, n] * np.sin(delta[m] - delta[n]) -
                                        B[m, n] * np.cos(delta[m] - delta[n]))

    # J2 (dP/dV)
    J2 = np.zeros((No_of_Bus - 1, No_of_PQ_Bus))
    for i in range(No_of_Bus - 1):
        m = i + 1
        for j in range(No_of_PQ_Bus):
            n = PQ_Bus[j]
            if m == n:
                # Elemento diagonal
                for k in range(No_of_Bus):
                    J2[i, j] += V[k] * (G[m, k] * np.cos(delta[m] - delta[k]) +
                                        B[m, k] * np.sin(delta[m] - delta[k]))
                J2[i, j] = J2[i, j] + V[m] * G[m, m]
            else:
                # Elemento fuera de diagonal
                J2[i, j] = V[m] * (G[m, n] * np.cos(delta[m] - delta[n]) +
                                    B[m, n] * np.sin(delta[m] - delta[n]))

    # J3 (dQ/dTheta)
    J3 = np.zeros((No_of_PQ_Bus, No_of_Bus - 1))
    for i in range(No_of_PQ_Bus):
        m = PQ_Bus[i]
        for j in range(No_of_Bus - 1):
            n = j + 1
            if m == n:
                # Elemento diagonal
                J3[i, j] = P[m] - V[m]**2 * G[m, m]
            else:
                # Elemento fuera de diagonal
                J3[i, j] = V[m] * V[n] * (-G[m, n] * np.cos(delta[m] - delta[n]) -
                                        B[m, n] * np.sin(delta[m] - delta[n]))

    # J4 (dQ/dV)
    J4 = np.zeros((No_of_PQ_Bus, No_of_PQ_Bus))
    for i in range(No_of_PQ_Bus):
        m = PQ_Bus[i]
        for j in range(No_of_PQ_Bus):
            n = PQ_Bus[j]
            if m == n:
                # Elemento diagonal
                for k in range(No_of_Bus):
                    J4[i, j] += V[k] * (G[m, k] * np.sin(delta[m] - delta[k]) -
                                        B[m, k] * np.cos(delta[m] - delta[k]))
                J4[i, j] = J4[i, j] - V[m] * B[m, m]
            else:
                # Elemento fuera de diagonal
                J4[i, j] = V[m] * (G[m, n] * np.sin(delta[m] - delta[n]) -
                                    B[m, n] * np.cos(delta[m] - delta[n]))

    J = np.block([[J1, J2], [J3, J4]])
    return J
def Newton_Raphson(busdata, gen_data_raw, G, B, No_of_Bus, BMva,gd_plan):
    bus_type = busdata[:, 1].astype(int)  # 3=Slack, 2=PV, 1=PQ
    V = busdata[:, 7].copy()  # ← Mejor inicialización
    delta = np.deg2rad(busdata[:, 8].copy())  # ← Usar ángulos iniciales

    Pd = busdata[:, 2] / BMva
    Qd = busdata[:, 3] / BMva

    # Crear vectores Pg, Qg, Qmin, Qmax inicializados en cero
    Pg = np.zeros(No_of_Bus)
    Qg = np.zeros(No_of_Bus)
    Qmin = np.full(No_of_Bus, -999.0)
    Qmax = np.full(No_of_Bus, 999.0)

    # Llenar con datos de generadores
    for gen in gen_data_raw:
        bus_idx = int(gen[0]) - 1
        Pg[bus_idx] = gen[1] / BMva
        Qg[bus_idx] = gen[2] / BMva
        Qmax[bus_idx] = gen[3] / BMva
        Qmin[bus_idx] = gen[4] / BMva
        V[bus_idx] = gen[5]  # Voltaje especificado del generador (sobrescribe)
    # Incorporar generación distribuida (GD) según el plan
    for bus, mw in gd_plan:
        bus_idx = bus - 1
        Pg[bus_idx] += mw / BMva  # Añadir generación activa de GD

    Pl = Pd.copy()
    Ql = Qd.copy()

    # Identify bus types (usando notación estándar)
    Slack_Bus = np.where(bus_type == 3)[0]
    PV_Bus = np.where(bus_type == 2)[0]
    PQ_Bus = np.where(bus_type == 1)[0]

    No_of_PQ_Bus = len(PQ_Bus)
    No_of_PV_Bus = len(PV_Bus)

    print(f"\nClasificación de buses:")
    print(f"Buses PV: {No_of_PV_Bus}")
    print(f"Buses PQ: {No_of_PQ_Bus}")
    print(f"Bus Slack: {Slack_Bus + 1}")
    print(f"Buses PV: {PV_Bus + 1}")
    print(f"Buses PQ: {PQ_Bus + 1}")

    Active_Power_specified = Pg - Pl
    Reactive_Power_specified = Qg - Ql

    # ============================================
    # NEWTON-RAPHSON LOAD FLOW
    # ============================================
    Iter = 1
    Tol = 1
    max_iterations = 100

    print("\n" + "=" * 70)
    print("INICIANDO ITERACIONES NEWTON-RAPHSON")
    print("=" * 70)

    while Tol > 1e-5 and Iter < max_iterations:
        # Calculate P and Q
        P = np.zeros(No_of_Bus)
        Q = np.zeros(No_of_Bus)

        for i in range(No_of_Bus):
            for j in range(No_of_Bus):
                P[i] += V[i] * V[j] * (G[i, j] * np.cos(delta[i] - delta[j]) +
                                        B[i, j] * np.sin(delta[i] - delta[j]))
                Q[i] += V[i] * V[j] * (G[i, j] * np.sin(delta[i] - delta[j]) -
                                        B[i, j] * np.cos(delta[i] - delta[j]))

        # Calculate mismatches
        dPa = Active_Power_specified - P
        dQa = Reactive_Power_specified - Q

        # Mismatches excluyendo Slack
        dP = dPa[1:No_of_Bus]  # Excluir bus 0 (Slack)

        dQ = np.zeros(No_of_PQ_Bus)
        for k, i in enumerate(PQ_Bus):
            dQ[k] = dQa[i]
        M = np.concatenate([dP, dQ])
        J = construir_Jacobiano(V, delta, G, B, P, No_of_Bus, PQ_Bus)
        X = np.linalg.solve(J, M)

        dTh = X[0:No_of_Bus - 1]
        dV = X[No_of_Bus - 1:]

        delta[1:No_of_Bus] = delta[1:No_of_Bus] + dTh

        for k, n in enumerate(PQ_Bus):
            V[n] = V[n] + dV[k]

        Iter += 1
        Tol = np.max(np.abs(M))

        print(f"Iteración {Iter-1}: Tolerancia = {Tol:.8f}")

    # ============================================
    # FINAL CALCULATION
    # ============================================
    P = np.zeros(No_of_Bus)
    Q = np.zeros(No_of_Bus)

    for i in range(No_of_Bus):
        for j in range(No_of_Bus):
            P[i] += V[i] * V[j] * (G[i, j] * np.cos(delta[i] - delta[j]) +
                                    B[i, j] * np.sin(delta[i] - delta[j]))
            Q[i] += V[i] * V[j] * (G[i, j] * np.sin(delta[i] - delta[j]) -
                                    B[i, j] * np.cos(delta[i] - delta[j]))

    delta_deg = np.rad2deg(delta)
        # Retornar resultados en un diccionario
    resultados = {
        'V': V,                           # Magnitudes de voltaje (pu)
        'delta': delta,                   # Ángulos (radianes)
        'delta_deg': delta_deg,           # Ángulos (grados)
        'P': P,                           # Potencias activas calculadas (pu)
        'Q': Q,                           # Potencias reactivas calculadas (pu)
        'Pg': Pg,                         # Generación activa (pu)
        'Qg': Qg,                         # Generación reactiva (pu)
        'Pl': Pl,                         # Carga activa (pu)
        'Ql': Ql,                         # Carga reactiva (pu)
        'bus_type': bus_type,             # Tipo de cada bus
        'iteraciones': Iter - 1,          # Número de iteraciones
        'Slack_Bus': Slack_Bus,           # Índice del bus Slack
        'PV_Bus': PV_Bus,                 # Índices de buses PV
        'PQ_Bus': PQ_Bus,                 # Índices de buses PQ
        'BMva': BMva,                     # Base de potencia
        'No_of_Bus': No_of_Bus            # Número de buses
    }
    return resultados
def Mostrar_resultados(resultados):
    # Extraer datos del diccionario de resultados
    V = resultados['V']
    delta_deg = resultados['delta_deg']
    P = resultados['P']
    Q = resultados['Q']
    Pg = resultados['Pg']
    Pl = resultados['Pl']
    Ql = resultados['Ql']
    bus_type = resultados['bus_type']
    BMva = resultados['BMva']
    No_of_Bus = resultados['No_of_Bus']
    Slack_Bus = resultados['Slack_Bus']
    
    # ============================================
    # TABLA DE RESULTADOS POR BUS
    # ============================================
    print("\n" + "=" * 90)
    print("                    NEWTON-RAPHSON LOAD FLOW SOLUTION")
    print("=" * 90)
    print(f"{'Bus':<5} {'Type':<7} {'Voltage':<10} {'Angle':<10} {'Pg':<10} {'Qg':<10} {'Pl':<10} {'Ql':<10}")
    print(f"{'No.':<5} {'':<7} {'(pu)':<10} {'(deg)':<10} {'(MW)':<10} {'(MVAr)':<10} {'(MW)':<10} {'(MVAr)':<10}")
    print("=" * 90)

    tipo_map = {3: 'Slack', 2: 'PV', 1: 'PQ'}
    Pg_val_total = 0
    Qg_val_total = 0
    
    for m in range(No_of_Bus):
        tipo = tipo_map[bus_type[m]]
        Pg_val = Pg[m] * BMva
        Pl_val = Pl[m] * BMva
        Ql_val = Ql[m] * BMva

        if bus_type[m] == 2 or bus_type[m] == 3:  # PV o Slack
            Qg_val = (Q[m] + Ql[m]) * BMva
            print(f"{m+1:<5} {tipo:<7} {V[m]:<10.4f} {delta_deg[m]:<10.4f} "
                  f"{Pg_val:<10.3f} {Qg_val:<10.3f} {Pl_val:<10.3f} {Ql_val:<10.3f}")
            Pg_val_total += Pg_val
            Qg_val_total += Qg_val
        else:  # PQ
            print(f"{m+1:<5} {tipo:<7} {V[m]:<10.4f} {delta_deg[m]:<10.4f} "
                  f"{Pg_val:<10.3f} {'---':<10} {Pl_val:<10.3f} {Ql_val:<10.3f}")

    print("=" * 90)
    print(f"Número de iteraciones: {resultados['iteraciones']}")
    
    # ============================================
    # RESUMEN DEL SISTEMA
    # ============================================
    P_gen_total_bruta = Pg_val_total
    P_gen_total = np.sum(P[P > 0]) * BMva
    P_load_total = np.sum(Pl) * BMva
    P_loss = P_gen_total - P_load_total

    Q_gen_total_bruta = Qg_val_total
    Q_gen_total = np.sum(Q[Q > 0]) * BMva
    Q_load_total = np.sum(Ql) * BMva
    Q_loss = Q_gen_total - Q_load_total

    print("\n" + "=" * 90)
    print("                            RESUMEN DEL SISTEMA")
    print("=" * 90)
    print(f"{'POTENCIA ACTIVA (MW)':<40} {'POTENCIA REACTIVA (MVAr)':<40}")
    print("-" * 90)
    print(f"{'Generación total (bruta):':<40} {P_gen_total_bruta:>10.2f}      "
          f"{'Generación total (bruta):':<40} {Q_gen_total_bruta:>10.2f}")
    print(f"{'Generación total (neto):':<40} {P_gen_total:>10.4f}      "
          f"{'Generación total (neto):':<40} {Q_gen_total:>10.4f}")
    print(f"{'Demanda total:':<40} {P_load_total:>10.4f}      "
          f"{'Demanda total:':<40} {Q_load_total:>10.4f}")
    print(f"{'Pérdidas del sistema:':<40} {P_loss:>10.4f}      "
          f"{'Pérdidas del sistema:':<40} {Q_loss:>10.4f}")
    print(f"{'% Pérdidas:':<40} {100*P_loss/P_gen_total:>10.2f}%")
    
    # ============================================
    # VALIDACIÓN - BUS SLACK
    # ============================================
    print("\n" + "=" * 90)
    print("                        VALIDACIÓN - BUS SLACK")
    print("=" * 90)
    Slack_idx = Slack_Bus[0]
    P_slack = (P[Slack_idx] + Pl[Slack_idx]) * BMva
    Q_slack = (Q[Slack_idx] + Ql[Slack_idx]) * BMva
    print(f"Bus Slack (Bus {Slack_idx + 1}):")
    print(f"  Generación P: {P_slack:.2f} MW")
    print(f"  Generación Q: {Q_slack:.2f} MVAr")
    print(f"  Voltaje: {V[Slack_idx]:.4f} pu")
    print(f"  Ángulo: {delta_deg[Slack_idx]:.2f}°")
    print("=" * 90)
def caso_base():
    print("=" * 70)
    print("FLUJO DE POTENCIA - MÉTODO DE NEWTON-RAPHSON")
    print("Sistema IEEE 30 Buses - Datos de MATPOWER")
    print("=" * 70)
    busdata, gen_data_raw, linedata = importar_datos()
    No_of_Bus = busdata.shape[0]
    BMva = 100
    Y = construir_Ybus(linedata, busdata,No_of_Bus,BMva)
    # Recalcular G y B después de agregar shunts
    G = np.real(Y)
    B = np.imag(Y)
    resultados = Newton_Raphson(busdata, gen_data_raw, G, B, No_of_Bus, BMva,[])
    menu_dos(resultados)
def caso_modificado_10():
    print("=" * 70)
    print("FLUJO DE POTENCIA - MÉTODO DE NEWTON-RAPHSON")
    print("Sistema IEEE 30 Buses - Datos de MATPOWER")
    print("=" * 70)
    busdata, gen_data_raw, linedata = importar_datos()
    # Modificar cargas en un 10%
    busdata[:, 2] *= 1.10  # Aumentar Pd en un 10%
    busdata[:, 3] *= 1.10  # Aumentar Qd en un 10%
    No_of_Bus = busdata.shape[0]
    BMva = 100
    Y = construir_Ybus(linedata, busdata,No_of_Bus,BMva)
    # Recalcular G y B después de agregar shunts
    G = np.real(Y)
    B = np.imag(Y)
    resultados = Newton_Raphson(busdata, gen_data_raw, G, B, No_of_Bus, BMva,[])
    menu_dos(resultados)
def opciones_menu():
    opcion=input("¿Desea volver al menú pricipal? (s/n): ")
    if opcion=="s":
        main()
    else:
        exit()
def menu_dos(resultados):
    while True:
        print("\nSeleccione una opción adicional:")
        print("1. Mostrar resultados del flujo de potencia")
        print("2. Calcular y mostrar corrientes en las líneas de transmisión")
        print("3. Volver al menú principal")
        opcion = input("Ingrese el número de la opción deseada: ")
        if opcion == "1":
            Mostrar_resultados(resultados)
            graficar_voltajes(resultados)
            opciones_menu()
        elif opcion == "2":
            Corrientes_linea(resultados)
            opciones_menu()
        elif opcion == "3":
            break   
def caso_generacion_distribuida():
    print("=" * 70)
    print("FLUJO DE POTENCIA - MÉTODO DE NEWTON-RAPHSON")
    print("Sistema IEEE 30 Buses - Datos de MATPOWER")
    print("=" * 70)
    busdata, gen_data_raw, linedata = importar_datos()
    Total_GD_P = 50  # MW
    FP_GD = 1  # Factor de potencia
    Total_GD_Q = Total_GD_P * np.tan(np.arccos(FP_GD))  # MVAr
    bus_kV_map = {int(b): int(kv) for b, kv in zip(busdata[:,0], busdata[:,9])}
    candidate_buses = [int(bus) for bus, kv in bus_kV_map.items() if kv == 33]
    print(f"Buses candidatos para GD (33kV): {candidate_buses}")
    # Seleccionaremos 5 buses para adicionar GD de manera equitativa
    gd_plan=[(19,10),(21,10),(24,10),(29,10),(30,10)]
    No_of_Bus = busdata.shape[0]
    BMva = 100
    Y = construir_Ybus(linedata, busdata,No_of_Bus,BMva)
    # Recalcular G y B después de agregar shunts
    G = np.real(Y)
    B = np.imag(Y)
    resultados = Newton_Raphson(busdata, gen_data_raw, G, B, No_of_Bus, BMva,gd_plan)
    menu_dos(resultados)
def Corrientes_linea(resultados):
    flujos = []
    V = resultados['V']
    delta = resultados['delta']
    BMva = resultados['BMva']
    No_of_Bus = resultados['No_of_Bus']
    busdata, gen_data_raw, linedata = importar_datos()
    Y = construir_Ybus(linedata, busdata,No_of_Bus,BMva)
    fb = linedata[:, 0].astype(int)
    tb = linedata[:, 1].astype(int)
    r = linedata[:, 2]
    x = linedata[:, 3]
    b_total = linedata[:, 4]
    a = linedata[:, 5]

    z = r + 1j * x
    y = 1.0 / z

    nl = len(fb)
    I_from = np.zeros(nl, dtype=complex)
    I_to = np.zeros(nl, dtype=complex)
    print("\n" + "=" * 84)
    print("|     Branch Data                                                              |")
    print("=" * 84)
    print("Brnch   From   To    From Bus Injection   To Bus Injection     Loss (I^2 * Z)  ")
    print("  #     Bus    Bus    P (MW)   Q (MVAr)   P (MW)   Q (MVAr)   P (MW)   Q (MVAr)")
    print("-----  -----  -----  --------  --------  --------  --------  --------  --------")
    for k in range(nl):
        fbus = int(linedata[k, 0]) - 1
        tbus = int(linedata[k, 1]) - 1
        i = fb[k] - 1
        j = tb[k] - 1
        V_i = V[i] * np.exp(1j * delta[i])
        V_j = V[j] * np.exp(1j * delta[j])
        I_from[k] = (V_i / a[k]- V_j) * y[k]
        I_to[k] = (V_j - V_i/ a[k]) * y[k]
        # Potencias complejas
        S_ft = V_i/a[k] * np.conj(I_from[k]) * BMva
        S_tf = V_j * np.conj(I_to[k]) * BMva

        P_from = np.real(S_ft)
        Q_from = np.imag(S_ft)
        P_to = np.real(S_tf)
        Q_to = np.imag(S_tf)

        P_loss = P_from + P_to
        Q_loss = Q_from + Q_to

        flujos.append({'P_loss': P_loss, 'Q_loss': Q_loss}) # Añadir las pérdidas a la lista

        print(f"{k+1:4d}   {fbus+1:4d}   {tbus+1:4d}   "
            f"{P_from:8.2f}  {Q_from:8.2f}  "
            f"{P_to:8.2f}  {Q_to:8.2f}  "
            f"{P_loss:8.3f}  {Q_loss:8.2f}")
    print("=" * 84)
    # Verificación: suma de pérdidas
    P_loss_total = sum([flujos[k]['P_loss'] for k in range(len(flujos))]) if flujos else 0
    Q_loss_total = sum([flujos[k]['Q_loss'] for k in range(len(flujos))]) if flujos else 0
    print(f"\nPérdidas totales del sistema: {P_loss_total:.4f} MW")
    print(f"Pérdidas totales del sistema: {Q_loss_total:.4f} MVAr")
def fallas_simetricas():
    V_fallas = []
    busdata, gen_data_raw, linedata = importar_datos()
    No_of_Bus = busdata.shape[0]
    BMva = 100
    Y = construir_Ybus(linedata, busdata, No_of_Bus, BMva)
    Z_bus = np.linalg.inv(Y)
    
    # Solicitar nodo de falla
    while True:
        nodo = int(input("Ingrese el número de nodo para la falla simétrica (1 - 30): "))
        if 1 <= nodo <= No_of_Bus:
            break
        else:
            print("Número de nodo inválido. Intente nuevamente.")
    
    # Flujo de potencia pre-falla
    resultados = Newton_Raphson(busdata, gen_data_raw, np.real(Y), np.imag(Y), No_of_Bus, BMva, [])
    V = resultados['V']
    delta = resultados['delta']
    
    # Corriente de falla total
    V_falla = V[nodo-1] * np.exp(1j * delta[nodo-1])
    I_falla = V_falla / Z_bus[nodo-1, nodo-1]
    # Calcular voltajes en todos los buses
    for i in range(No_of_Bus):
        V_i = V[i] * np.exp(1j * delta[i])
        dV = -Z_bus[i, nodo-1] * I_falla
        V_resultado = V_i + dV
        V_fallas.append(V_resultado)

    # ============================================
    # TABLA DE RESULTADOS
    # ============================================
    print("\n" + "=" * 100)
    print("                    VOLTAJES Y CORRIENTES DURANTE LA FALLA")
    print("=" * 100)
    print(f"{'Bus':<5} {'V pre (pu)':<12} {'V post (pu)':<12} {'∠V (°)':<10} ")
    print("-" * 100)
    
    for i in range(No_of_Bus):
        V_mag_pre = V[i]  
        V_mag_post = np.abs(V_fallas[i])
        V_ang_post = np.rad2deg(np.angle(V_fallas[i]))
        # Marcar el nodo de falla
        marca = " ← FALLA" if i == nodo-1 else ""
        print(f"{i+1:<5} {V_mag_pre:<12.4f} {V_mag_post:<12.4f} {V_ang_post:<10.2f} "+ marca)
    
    print("=" * 100)
    V_fallas_mag = [np.abs(v) for v in V_fallas]
    delta_falla = [np.angle(v) for v in V_fallas]
    resultados_falla = {
        'V': V_fallas_mag,
        'delta': delta_falla,
        'BMva': BMva,
        'No_of_Bus': No_of_Bus,
    }
    corrientes_fallas_lineas(resultados_falla,I_falla)
    # Llamar a análisis de todas las fallas
    respuesta2 = input("\n¿Desea ver el análisis comparativo de la falla en los nodos? (s/n): ")
    if respuesta2.lower() == 's':
        graficar_tensiones_falla_base(V, [np.abs(v) for v in V_fallas], nodo)
    
    respuesta = input("\n¿Desea ver el análisis comparativo de fallas en TODOS los nodos? (s/n): ")
    if respuesta.lower() == 's':
        fallas_todos_los_nodos()
    
    opciones_menu()
def graficar_voltajes(resultados):
    buses = np.arange(1, resultados['No_of_Bus'] + 1)
    V = resultados['V']
    
    plt.figure(figsize=(12, 5))
    plt.plot(buses, V, 'o-', linewidth=2)
    plt.axhline(y=1.06, color='r', linestyle='--', label='Vmax')
    plt.axhline(y=0.94, color='r', linestyle='--', label='Vmin')
    plt.xlabel('Bus Number')
    plt.ylabel('Voltage (pu)')
    plt.title('Perfil de Voltajes del Sistema')
    plt.grid(True)
    plt.legend()
    plt.show()
def fallas_todos_los_nodos():
    from __main__ import importar_datos, construir_Ybus
    
    busdata, gen_data_raw, linedata = importar_datos()
    No_of_Bus = busdata.shape[0]
    BMva = 100
    Y = construir_Ybus(linedata, busdata, No_of_Bus, BMva)
    Z_bus = np.linalg.inv(Y)
    resultados= Newton_Raphson(busdata, gen_data_raw, np.real(Y), np.imag(Y), No_of_Bus, BMva, [])
    # Voltajes y ángulos pre-falla
    V_prefalla = resultados['V'].copy()
    delta_prefalla = np.rad2deg(resultados['delta'].copy())
    
    buses = np.arange(1, No_of_Bus + 1)
    
    # Crear figura
    plt.figure(figsize=(14, 8))
    
    print("Simulando fallas en todos los nodos...")
    
    # Para cada nodo de falla
    for nodo_falla in range(No_of_Bus):
        # Voltaje pre-falla en el nodo de falla
        V_nodo = V_prefalla[nodo_falla] * np.exp(1j * delta_prefalla[nodo_falla])
        
        # Corriente de falla
        I_falla = V_nodo / Z_bus[nodo_falla, nodo_falla]
        
        # Calcular voltajes en todos los buses durante la falla
        V_durante_falla = []
        for i in range(No_of_Bus):
            V_i = V_prefalla[i] * np.exp(1j * delta_prefalla[i])
            dV = -Z_bus[i, nodo_falla] * I_falla
            V_resultado = V_i + dV
            V_durante_falla.append(np.abs(V_resultado))
        
        # Graficar perfil de voltaje para esta falla
        plt.plot(buses, V_durante_falla, 'o-', alpha=0.6, linewidth=1, 
                markersize=3, label=f'Falla Bus {nodo_falla + 1}')
    
    plt.xlabel('Número de Bus', fontsize=12, fontweight='bold')
    plt.ylabel('Voltaje (pu)', fontsize=12, fontweight='bold')
    plt.title('Perfiles de Voltaje del Sistema para Fallas en Cada Nodo', 
              fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0.9, color='red', linestyle='--', linewidth=2, label='Límite 0.9 pu')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=8, ncol=2)
    plt.tight_layout()
    plt.show()
def graficar_tensiones_falla_base(V, V_falla, nodo):
    buses = np.arange(1, len(V) + 1)
    plt.figure(figsize=(12, 5))
    plt.plot(buses, V, 'o-', label='Voltaje Pre-Falla', linewidth=2)
    plt.plot(buses, V_falla, 's--', label='Voltaje Durante Falla', linewidth=2)
    plt.axhline(y=1.06, color='r', linestyle='--', label='Vmax')
    plt.axhline(y=0.94, color='r', linestyle='--', label='Vmin')
    plt.xlabel('Número de Bus')
    plt.ylabel('Voltaje (pu)')
    plt.title(f'Perfil de Voltajes - Falla en el Bus {nodo}')
    plt.grid(True)
    plt.legend()
    plt.show()
def corrientes_fallas_lineas(resultados,I_falla):
    V = resultados['V']
    delta = resultados['delta']
    BMva = resultados['BMva']
    No_of_Bus = resultados['No_of_Bus']
    busdata, gen_data_raw, linedata = importar_datos()
    fb = linedata[:, 0].astype(int)
    tb = linedata[:, 1].astype(int)
    r = linedata[:, 2]
    x = linedata[:, 3]
    Z_linea = r + 1j * x
    nl = len(fb)
    I_falla_total_mag = np.abs(I_falla)
    print("corriente de falla total (pu):",I_falla_total_mag)
    print("\n" + "=" * 84)
    print("|     I Líneas CC                                                         |")
    print("=" * 84)
    print("Brnch   From   To    I  ")
    print("  #     Bus    Bus    I (pu)   ∠I (°)   % I_falla")
    print("-----  -----  -----  --------  --------  --------  ")
    for k in range(nl):
        fbus = int(linedata[k, 0]) - 1
        tbus = int(linedata[k, 1]) - 1
        i = fb[k] - 1
        j = tb[k] - 1
        if np.abs(Z_linea[k]) != 0:
            I_linea = (V[i] * np.exp(1j * delta[i]) - V[j] * np.exp(1j * delta[j])) / Z_linea[k]
        else:
            I_linea = 0
        I_mag = np.abs(I_linea)
        I_ang_deg = np.rad2deg(np.angle(I_linea))
        
        if I_falla_total_mag != 0:
            porcentaje_I_falla = (I_mag / I_falla_total_mag) * 100
        else:
            porcentaje_I_falla = 0
        print(f"{k+1:4d}   {fbus+1:4d}   {tbus+1:4d}   "
            f"{I_mag:8.2f}  {I_ang_deg:8.2f}  "
            f"{porcentaje_I_falla:8.2f}")

    print("=" * 84)
def despacho_economico(a, b, Pmin, Pmax, PD, tol=1e-6, max_iter=200):
    lam_low = min(b)
    lam_high = max(b + 2*a*Pmax)
    
    def allocate(lam):
        """Asigna generación según lambda, respetando límites"""
        P = (lam - b) / (2*a)
        return np.clip(P, Pmin, Pmax)
    
    for _ in range(max_iter):
        lam_mid = 0.5 * (lam_low + lam_high)
        P = allocate(lam_mid)
        error = PD - P.sum()
        
        if abs(error) < tol:
            return P, lam_mid, True
        
        if error > 0:
            lam_low = lam_mid
        else:
            lam_high = lam_mid
    
    return P, lam_mid, False
def importar_despacho():
    # --- Datos de costo (mpc.gencost) ---
    gencost = np.array([
        [2, 0, 0, 3, 0.03843, 20, 0],
        [2, 0, 0, 3, 0.25, 20, 0],
        [2, 0, 0, 3, 0.01, 40, 0],
        [2, 0, 0, 3, 0.01, 40, 0],
        [2, 0, 0, 3, 0.01, 40, 0],
        [2, 0, 0, 3, 0.01, 40, 0]
    ])
    gen_data_raw = np.array([
    [1,  260.2, -16.1, 10,  0,    1.06, 100, 1, 360.2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [2,   40.0,  50.0, 50, -40,   1.045,100, 1, 140.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [5,    0.0,  37.0, 40, -40,   1.01, 100, 1, 100.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [8,    0.0,  37.3, 40, -10,   1.01, 100, 1, 100.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [11,   0.0,  16.2, 24, -6,    1.082,100, 1, 100.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [13,   0.0,  10.6, 24, -6,    1.071,100, 1, 100.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])
    n_gen = gencost.shape[0]
    a = np.zeros(n_gen)
    b = np.zeros(n_gen)
    c = np.zeros(n_gen)
    Pmax   = gen_data_raw[:, 8]
    Pmin   = gen_data_raw[:, 9]
    for i in range(n_gen):
        n = int(gencost[i, 3])  # grado polinomio +1
        coeffs = gencost[i, 4:4+n]
        if n == 3:
            a[i] = coeffs[0]
            b[i] = coeffs[1]
            c[i] = coeffs[2]
        else:
            raise ValueError("Solo se soporta polinomio cuadrático (grado 2)")

    
    return a, b, c, Pmin, Pmax
def despacho_uno():
    busdata, gen_data_raw, linedata = importar_datos()
    No_of_Bus = busdata.shape[0]
    BMva = 100
    Y = construir_Ybus(linedata, busdata,No_of_Bus,BMva)
    # Recalcular G y B después de agregar shunts
    G = np.real(Y)
    B = np.imag(Y)
    resultados = Newton_Raphson(busdata, gen_data_raw, G, B, No_of_Bus, BMva,[])
    a, b, c, Pmin, Pmax = importar_despacho()
    PD = np.sum(resultados['Pl'])
    P_base, lam_base, conv_base = despacho_economico(a, b, Pmin, Pmax, PD)
    P_final=P_base*BMva
    costo_individual = a*P_final**2 + b*P_final + c
    costo_total = np.sum(costo_individual)
    
    # Mostrar resultados
    print("----- DESPACHO ECONÓMICO -----")
    print(f"Demanda total (PD): {PD:.3f} pu")
    print(f"Lambda óptima: {lam_base:.3f}")
    print(f"Convergencia: {conv_base}\n")
    print("Generador | P asignada (MW) | Costo ($/h)")
    for i in range(len(P_base)):
        print(f"{i+1:>9} | {P_base[i]:>13.3f} | {costo_individual[i]:>10.3f}")
    print(f"\nCosto total del despacho: {costo_total:.3f} $/h")
    opciones_menu()
def despacho_dos():
    busdata, gen_data_raw, linedata = importar_datos()
    # Modificar cargas en un 10%
    busdata[:, 2] *= 1.10  # Aumentar Pd en un 10%
    busdata[:, 3] *= 1.10  # Aumentar Qd en un 10%
    No_of_Bus = busdata.shape[0]
    BMva = 100
    Y = construir_Ybus(linedata, busdata,No_of_Bus,BMva)
    # Recalcular G y B después de agregar shunts
    G = np.real(Y)
    B = np.imag(Y)
    a, b, c, Pmin, Pmax = importar_despacho()
    resultados = Newton_Raphson(busdata, gen_data_raw, G, B, No_of_Bus, BMva, [])
    PD = np.sum(resultados['Pl'])
    P_base, lam_base, conv_base = despacho_economico(a, b, Pmin, Pmax, PD)
    P_final=P_base*BMva
    costo_individual = a*P_final**2 + b*P_final + c
    costo_total = np.sum(costo_individual)
    
    # Mostrar resultados
    print("----- DESPACHO ECONÓMICO -----")
    print(f"Demanda total (PD): {PD:.3f} pu")
    print(f"Lambda óptima: {lam_base:.3f}")
    print(f"Convergencia: {conv_base}\n")
    print("Generador | P asignada (pu) | Costo ($/h)")
    for i in range(len(P_base)):
        print(f"{i+1:>9} | {P_base[i]:>13.3f} | {costo_individual[i]:>10.3f}")
    print(f"\nCosto total del despacho: {costo_total:.3f} $/h")
    opciones_menu()
def despacho_tres():
    busdata, gen_data_raw, linedata = importar_datos()
    
    # --- Configuración DG ---
    P_DG_total = 50/100  # generación total de DG en pu
    # Distribución equitativa de DG en los buses seleccionados
    gd_plan = [(19,10),(21,10),(24,10),(29,10),(30,10)]  # (bus, Ppu)
    
    No_of_Bus = busdata.shape[0]
    BMva = 100
    Y = construir_Ybus(linedata, busdata, No_of_Bus, BMva)
    G = np.real(Y)
    B = np.imag(Y)
    
    # Ejecutar Newton-Raphson incluyendo GD (solo para flujo)
    resultados = Newton_Raphson(busdata, gen_data_raw, G, B, No_of_Bus, BMva, gd_plan)
    
    # --- Importar costos y límites ---
    a, b, c, Pmin, Pmax = importar_despacho()
    
    # --- Ajustar demanda para despacho económico ---
    PD_total = np.sum(resultados['Pl'])
    PD_conv = PD_total - P_DG_total  # demanda restante para unidades convencionales
    
    # --- Despacho económico para unidades convencionales ---
    P_conv, lambda_opt, conv = despacho_economico(a, b, Pmin, Pmax, PD_conv)
    
    # --- Agregar DG al resultado final ---
    P_final = np.append(P_conv, P_DG_total)
    # Costo de DG: lineal, a=0, b=10 (puedes ajustar según LCOE)
    a = np.append(a, 0.0)
    b = np.append(b, 35.0)
    c = np.append(c, 0.0)
    P_final = P_final * BMva  # Convertir a MW
    costo_individual = a*P_final**2 + b*P_final + c
    costo_total = np.sum(costo_individual)
    
    # --- Mostrar resultados ---
    print("----- DESPACHO ECONÓMICO CON DG -----")
    print(f"Demanda total (PD): {PD_total:.3f} pu")
    print(f"Lambda del sistema: {lambda_opt:.3f}, Convergencia: {conv}\n")
    print("Unidad | P asignada (pu) | Costo ($/h)")
    
    for i in range(len(P_final)):
        tipo = "DG" if i == len(P_final)-1 else "Gen"
        print(f"{tipo} {i+1:>2} | {P_final[i]:>13.3f} | {costo_individual[i]:>10.3f}")
    
    print(f"\nCosto total del despacho: {costo_total:.3f} $/h")
    opciones_menu()
def despacho_economico_distri(a, b, Pmin, Pmax, PD, tol=1e-6, max_iter=200):
    lam_low = min(b)
    lam_high = max(b + 2*a*Pmax)
    
    def allocate(lam):
        P = np.zeros_like(b)
        for i in range(len(b)):
            if a[i] == 0:  # costo lineal (DG)
                if lam > b[i]:
                    P[i] = Pmax[i]
                else:
                    P[i] = Pmin[i]
            else:  # costo cuadrático
                P[i] = (lam - b[i]) / (2*a[i])
                P[i] = np.clip(P[i], Pmin[i], Pmax[i])
        return P   
    
    for _ in range(max_iter):
        lam_mid = 0.5 * (lam_low + lam_high)
        P = allocate(lam_mid)
        error = PD - P.sum()
        
        if abs(error) < tol:
            return P, lam_mid, True
        
        if error > 0:
            lam_low = lam_mid
        else:
            lam_high = lam_mid
    
    return P, lam_mid, False

def main():
    print("=" * 70)
    print("FLUJO DE POTENCIA - MÉTODO DE NEWTON-RAPHSON")
    print("Sistema IEEE 30 Buses - Datos de MATPOWER")
    print("=" * 70)
    print("Modelo para la solción del Caso de Estudio, Sistema de Prueba IEEE 30 Buses\n")
    print("El sistema de prueba IEEE 30 Buses es un modelo clásico de un sistema de transmisión de mediana escala,\n diseñado para estudios de flujo de potencia, análisis de fallas y despacho económico.\n")
    print("Está compuesto por 30 nodos, 6 generadores, 24 cargas, 41 líneas de transmisión, y opera típicamente a dos niveles de tensión: 132kV y 33kV.\n")
    print("1. Ver Diagrama Unifilar del Sistema IEEE 30 Buses\n")
    print("2. Ejecutar Flujos de Potencia con diferentes escenarios\n")
    print("3. Análisis de fallas simetricas\n")
    print("4. Despacho Económico.\n")
    while True:
        Punto = input("Seleccione el punto a ejecutar: ")
        if Punto == '1':
             while True:
                print("Seleccione que inciso desea ejecutar:")
                print("a) Caso Base sin Modificaciones.")
                print("b) Caso Base con Modificaciones, aumento en el 10% en todas las cargas.")
                print("c) Caso Base con Generación Distribuida (50kW).")
                inciso = input("Ingrese a, b o c: ")
                if inciso == 'a':
                    print("Enlace de descarga: https://pruebacorreoescuelaingeduco-my.sharepoint.com/:b:/g/personal/sebastian_perez-l_mail_escuelaing_edu_co/IQA5FxXJRyxXSq_Y_XnMOY4yAWTA5dgWhdtNo8rm420vVlQ?e=XkDFSM")
                    opciones_menu()
                elif inciso == 'b':
                    print("Enlace de descarga: https://pruebacorreoescuelaingeduco-my.sharepoint.com/:b:/g/personal/sebastian_perez-l_mail_escuelaing_edu_co/IQDu0WvorA7TQ6Nd1u8lqQ3-AW9p19_lfBHZW86wcKN89-I?e=5NtcT5")
                    opciones_menu()
                elif inciso == 'c':
                    print("Enlace de descarga: https://pruebacorreoescuelaingeduco-my.sharepoint.com/:b:/g/personal/sebastian_perez-l_mail_escuelaing_edu_co/IQBwu15tQKAqQq7rt8jiPy3IAZiZb-gag8Px5R08yOerW34?e=DGzheM")
                    opciones_menu()
                else:
                    print("Opción inválida. Intente nuevamente.\n")
        elif Punto == '2':
            while True:
                print("Seleccione que inciso desea ejecutar:")
                print("a) Caso Base sin Modificaciones.")
                print("b) Caso Base con Modificaciones, aumento en el 10% en todas las cargas.")
                print("c) Caso Base con Generación Distribuida (50kW).")
                inciso = input("Ingrese a, b o c: ")
                if inciso == 'a':
                    caso_base()
                    break
                elif inciso == 'b':
                    caso_modificado_10()
                    break
                elif inciso == 'c':
                    caso_generacion_distribuida()
                    break
                else:
                    print("Opción inválida. Intente nuevamente.\n")
        elif Punto == '3':
            fallas_simetricas()
        elif Punto == '4':
            while True:
                print("Seleccione que inciso desea ejecutar:")
                print("a) Caso Base sin Modificaciones.")
                print("b) Caso Base con Modificaciones, aumento en el 10% en todas las cargas.")
                print("c) Caso Base con Generación Distribuida (50kW).")
                inciso = input("Ingrese a, b o c: ")
                if inciso == 'a':
                    despacho_uno()
                    break
                elif inciso == 'b':
                    despacho_dos()
                    break
                elif inciso == 'c':
                    despacho_tres()
                    break
                else:
                    print("Opción inválida. Intente nuevamente.\n")
            
        else:

            print("Opción inválida. Intente nuevamente.\n")
main()