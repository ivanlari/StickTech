def eulAnim(solver_outputs, inputs_list):

    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.animation import FuncAnimation
    from mpl_toolkits.mplot3d import Axes3D
    from datetime import datetime
    import logging
    import os

    t_span  = solver_outputs[0]
    q       = solver_outputs[1]
    t_max   = solver_outputs[2]
    theta   = solver_outputs[3]
    alpha   = solver_outputs[4]
    h       = solver_outputs[5]
    gamma   = solver_outputs[6]
    beta    = solver_outputs[7]
    p       = solver_outputs[8]
    r       = solver_outputs[9]
    phi     = solver_outputs[10]
    u       = solver_outputs[11]
    w       = solver_outputs[12]
    psi     = solver_outputs[13]

    U0      = inputs_list[7]
    V0      = 0
    W0      = 0

    v       = beta*U0

    equilibratore   = inputs_list[13]
    alettone        = inputs_list[28]
    timone          = inputs_list[29]

    # Costruisci liste con comandi in input
    de_list = []
    da_list = []
    dr_list = []
    de_deg  = inputs_list[32]
    dr_deg  = inputs_list[35]
    da_deg  = inputs_list[38]

    for i in t_span:
        de_list.append(equilibratore(i)*de_deg)
        da_list.append(alettone(i)*da_deg)
        dr_list.append(timone(i)*dr_deg)

    # Velocità complessiva
    U = U0 + u
    V = V0 + v 
    W = W0 + w

    # Velocità angolari (deg/s)
    P0 = 0
    Q0 = 0
    R0 = 0
    P = P0 + p
    Q = Q0 + q
    R = R0 + r

    # Posizioni iniziali
    x0, y0, z0 = 0, 0, 0

    # Passo temporale
    dt = np.mean(np.diff(t_span))  # Supponendo che t_span sia uniforme

    # Integrazione numerica cumulativa delle velocità
    x = x0 + np.cumsum(U * dt)
    y = y0 + np.cumsum(V * dt)
    z = z0 + np.cumsum(W * dt)

    scale_factor = 1

    # Funzione per calcolare la matrice di rotazione a partire dagli angoli di Eulero (ordine X-Y-Z)
    def euler_to_rotation_matrix(roll, pitch, yaw):
        # Matrici di rotazione per ogni angolo
        R_x = np.array([[1, 0, 0],
                        [0, np.cos(roll), np.sin(roll)],
                        [0, -np.sin(roll), np.cos(roll)]])
        
        R_y = np.array([[np.cos(pitch), 0, -np.sin(pitch)],
                        [0, 1, 0],
                        [np.sin(pitch), 0, np.cos(pitch)]])
        
        R_z = np.array([[np.cos(yaw), np.sin(yaw), 0],
                        [-np.sin(yaw), np.cos(yaw), 0],
                        [0, 0, 1]])

        # Moltiplichiamo in ordine X-Y-Z
        return R_x @ R_y @ R_z

    def draw_airplane(ax, R):
        # Fusoliera
        fuselage_length = 2.0  # Lunghezza fusoliera
        fuselage_points = np.array([[-fuselage_length / 2, 0, 0], [fuselage_length / 2, 0, 0]])
        fuselage_rotated = (R @ fuselage_points.T).T
        ax.plot(fuselage_rotated[:, 0], fuselage_rotated[:, 1], fuselage_rotated[:, 2], color="blue", lw=4)

        # Ali
        wing_span = 2.8  # Larghezza alare
        wing_length = 0.3  # Lunghezza alare
        wing_points = np.array([
            [-wing_length / 2, -wing_span / 2, 0],
            [wing_length / 2, -wing_span / 2, 0],
            [wing_length / 2, wing_span / 2, 0],
            [-wing_length / 2, wing_span / 2, 0]
        ])
        wing_points = np.vstack([wing_points, wing_points[0]])  # Chiusura del poligono dell'ala
        wing_rotated = (R @ wing_points.T).T
        ax.plot(wing_rotated[:, 0], wing_rotated[:, 1], wing_rotated[:, 2], color="blue", lw=2)

        # Aggiungi linee parallele alle ali
        num_lines_wing = 0  # Numero di linee parallele da aggiungere
        for i in range(1, num_lines_wing):
            wing_inner_points = np.array([
                [-wing_length / 2, -wing_span / 2 + (i * wing_span / num_lines_wing), 0],
                [wing_length / 2, -wing_span / 2 + (i * wing_span / num_lines_wing), 0]
            ])
            wing_inner_rotated = (R @ wing_inner_points.T).T
            ax.plot(wing_inner_rotated[:, 0], wing_inner_rotated[:, 1], wing_inner_rotated[:, 2], color="blue", lw=1)

        # Coda verticale
        tail_height = 0.5  # Altezza coda verticale
        tail_width = 0.2  # Larghezza coda verticale
        tail_vertical_points = np.array([
            [-fuselage_length / 2, 0, 0],
            [-fuselage_length / 2, 0, tail_height],
            [-fuselage_length / 2 - tail_width, 0, tail_height],
            [-fuselage_length / 2 - tail_width, 0, 0],
            [-fuselage_length / 2, 0, 0]
        ])
        tail_vertical_rotated = (R @ tail_vertical_points.T).T
        ax.plot(tail_vertical_rotated[:, 0], tail_vertical_rotated[:, 1], tail_vertical_rotated[:, 2], color="blue", lw=2)

        # Aggiungi linee parallele alla coda verticale
        num_lines_tail_vertical = 0  # Numero di linee parallele alla coda verticale
        for i in range(1, num_lines_tail_vertical):
            tail_vertical_inner_points = np.array([
                [-fuselage_length / 2 - i * tail_width / num_lines_tail_vertical, 0, 0],
                [-fuselage_length / 2 - i * tail_width / num_lines_tail_vertical, 0, tail_height]
            ])
            tail_vertical_inner_rotated = (R @ tail_vertical_inner_points.T).T
            ax.plot(tail_vertical_inner_rotated[:, 0], tail_vertical_inner_rotated[:, 1], tail_vertical_inner_rotated[:, 2], color="blue", lw=1)

        # Coda orizzontale
        tail_horizontal_span = 0.8  # Larghezza coda orizzontale
        tail_horizontal_length = tail_width  # Lunghezza coda orizzontale
        tail_horizontal_points = np.array([
            [-fuselage_length / 2 - tail_horizontal_length / 2, -tail_horizontal_span / 2, 0],
            [-fuselage_length / 2 + tail_horizontal_length / 2, -tail_horizontal_span / 2, 0],
            [-fuselage_length / 2 + tail_horizontal_length / 2, tail_horizontal_span / 2, 0],
            [-fuselage_length / 2 - tail_horizontal_length / 2, tail_horizontal_span / 2, 0],
            [-fuselage_length / 2 - tail_horizontal_length / 2, -tail_horizontal_span / 2, 0]
        ])
        tail_horizontal_rotated = (R @ tail_horizontal_points.T).T
        ax.plot(tail_horizontal_rotated[:, 0], tail_horizontal_rotated[:, 1], tail_horizontal_rotated[:, 2], color="blue", lw=2)

        # Aggiungi linee parallele alla coda orizzontale
        num_lines_tail_horizontal = 0  # Numero di linee parallele alla coda orizzontale
        for i in range(1, num_lines_tail_horizontal):
            tail_horizontal_inner_points = np.array([
                [-fuselage_length / 2 - tail_horizontal_length / 2, -tail_horizontal_span / 2 + i * tail_horizontal_span / num_lines_tail_horizontal, 0],
                [-fuselage_length / 2 + tail_horizontal_length / 2, -tail_horizontal_span / 2 + i * tail_horizontal_span / num_lines_tail_horizontal, 0]
            ])
            tail_horizontal_inner_rotated = (R @ tail_horizontal_inner_points.T).T
            ax.plot(tail_horizontal_inner_rotated[:, 0], tail_horizontal_inner_rotated[:, 1], tail_horizontal_inner_rotated[:, 2], color="blue", lw=1)

    # Funzione per aggiornare la scena
    def update(frame):
        ax.cla()  # Pulisce l'asse
        ax.set_xlabel(f"X = {x[frame]:.2f} m")
        ax.set_ylabel(f"Y = {y[frame]:.2f} m")
        ax.set_zlabel(f"Z = {z[frame]:.2f} m")
        ax.set_xlim([-1, 1])
        ax.set_ylim([-1, 1])
        ax.set_zlim([-1, 1])
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        ax.get_zaxis().set_ticks([])
        #ax.grid(True)
        
        # Angoli di Eulero per il frame corrente
        roll, pitch, yaw = angles[frame]
        
        # Matrice di rotazione
        T = euler_to_rotation_matrix(roll, pitch, yaw)
        
        # Disegna l'aereo
        draw_airplane(ax, T)

        # Aggiorna il testo del tempo
        text_obj.set_text(f'Time: {t_span[frame]:.2f} s')

        # Aggiorna i valori di roll, pitch, yaw
        angle_text.set_text(f'$\\phi$ = {np.degrees(roll):.2f}°\n$\\theta$ = {np.degrees(pitch):.2f}°\n$\\psi$ = {np.degrees(yaw):.2f}°')

        # Aggiungi i valori degli inputs
        inputs_text.set_text(f'$\\delta_a$ = {da_list[frame]:.1f}°\n$\\delta_e$ = {de_list[frame]:.1f}°\n$\\delta_r$ = {dr_list[frame]:.1f}°')

        # Aggiungi i valori per U, V, W
        vel_text.set_text(f'$U$ = {U[frame]:.2f} $m/s$\n$V$ = {V[frame]:.2f} $m/s$\n$W$ = {W[frame]:.2f} $m/s$')

        # Aggiungi i valori per P, Q, R
        vel_ang_text.set_text(f'$P$ = {P[frame]:.2f} $deg/s$\n$Q$ = {Q[frame]:.2f} $deg/s$\n$R$ = {R[frame]:.2f} $deg/s$')

        return text_obj,

    roll_values = scale_factor*np.radians(phi)  # Rollio (X)
    pitch_values = scale_factor*np.radians(theta)  # Beccheggio (Y)
    yaw_values = scale_factor*np.radians(psi)  # Imbardata (Z)

    # Lista degli angoli (tutti iniziano a zero)
    angles = [(0, 0, 0)] + list(zip(roll_values, pitch_values, yaw_values))  # Il primo frame è (0,0,0)

    # Parametri dell'animazione
    total_duration = t_max  # Durata totale in secondi
    num_frames = len(t_span)

    # Calcola l'intervallo tra i fotogrammi in millisecondi
    interval = (total_duration / num_frames) * 1000  # in millisecondi

    # Calcola il frame rate per il salvataggio del video
    fps = num_frames / total_duration  # frame per secondo

    fig = plt.figure(figsize=(10, 8))

    # Crea due assi: uno per il grafico 3D e uno per il testo
    gs = fig.add_gridspec(2, 1, height_ratios=[0.9, 0.1])  # 90% per il grafico 3D, 10% per il testo
    ax = fig.add_subplot(gs[0], projection='3d')  # Grafico 3D
    ax_2d = fig.add_subplot(gs[1])  # Grafico 2D per il testo

    # Aggiungi il testo per il tempo nel grafico 2D
    text_obj = ax_2d.text(0.5, 0.5, f'Time: {t_span[0]:.2f} s', fontsize=12, color='black', ha='center')

    # Aggiungi il testo per i valori di roll, pitch, yaw
    angle_text = ax_2d.text(0.85, 1, f'$\\phi$ = {np.degrees(angles[0][0]):.2f}°\n$\\theta$ = {np.degrees(angles[0][1]):.2f}°\n$\\psi$ = {np.degrees(angles[0][2]):.2f}°', 
                            fontsize=12, color='black', ha='center')

    # Aggiungi i valori per de_deg, da_deg, e dr_deg
    inputs_text = ax_2d.text(0.15, 1, f'$\\delta_a$ = {da_list[0]:.1f}°\n$\\delta_e$ = {de_list[0]:.1f}°\n$\\delta_r$ = {dr_list[0]:.1f}°', 
                         fontsize=12, color='black', ha='center')
    
    # Aggiungi i valori per U, V, W
    vel_text = ax_2d.text(0.85, 10.5, f'$U$ = {U[0]:.2f} $m/s$\n$V$ = {V[0]:.2f} $m/s$\n$W$ = {W[0]:.2f} $m/s$', fontsize=12, color='black', ha='center')
    
    # Aggiungi i valori per P, Q, R
    vel_ang_text = ax_2d.text(0.15, 10.5, f'$P$ = {P[0]:.2f} $deg/s$\n$Q$ = {Q[0]:.2f} $deg/s$\n$R$ = {R[0]:.2f} $deg/s$', fontsize=12, color='black', ha='center')

    # Aggiungi testo per fattore di scala animazione
    text_obj_2 = ax_2d.text(0.5, 0.05, "Animation Scale Factor: " + str(scale_factor), fontsize=10, color='black', ha='center')

    ax_2d.axis('off')  # Disabilita gli assi del grafico 2D

    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Generating Aircraft Animation. Please wait...")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Generating Aircraft Animation...")

    # Crea l'animazione
    ani = FuncAnimation(fig, update, frames=num_frames, interval=interval)

    # Salva l'animazione in MP4 senza visualizzarla
    ani.save('Aircraft_Animation.mp4', writer='ffmpeg', fps=fps)  # Salva con fps sincronizzato

    print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Aircraft Animation generated.")
    logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Aircraft Animation generated.")

    #os.system("Aircraft_Animation.mp4")