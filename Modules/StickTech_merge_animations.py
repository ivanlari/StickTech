def mergeAnim():

    from moviepy import VideoFileClip, clips_array
    import logging
    from datetime import datetime

    ask_merge = input("Would you like to generate a complete Aircraft Animation? (y/n): ")

    if ask_merge == "y":
        # Carica i video
        video1 = VideoFileClip('Aircraft_Animation.mp4')
        video2 = VideoFileClip('Longitudinal_Dynamics_Animation.mp4')
        video3 = VideoFileClip('LateralDirectional_Dynamics_Animation.mp4')

        # Ridimensiona i video
        # Video a sinistra sarà più grande (ad esempio 1.5x più grande degli altri)
        video1 = video1.resized(1.8)  # Aumenta la dimensione del primo video (video1)
        video2 = video2.resized(height=720)  # Mantieni l'altezza del video2 a 720px
        video3 = video3.resized(height=720)  # Mantieni l'altezza del video3 a 720px

        # Calcola la larghezza finale
        final_width = video1.size[0] + video2.size[0]  # Larghezza video1 + video2
        final_height = max(video1.size[1], video2.size[1] + video3.size[1])  # Altezza massima tra video1 e la colonna video2-video3

        # Combina i video (video2 e video3 sono messi uno sopra l'altro)
        right_column = clips_array([[video2], [video3]])

        # Unisci il primo video a sinistra con la colonna dei due video a destra
        final_video = clips_array([[video1, right_column]])

        print(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Generating Complete aircraft Animation. Please wait...")
        logging.info(datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "    Generating Complete aircraft Animation...")

        # Esporta il video finale in formato mp4
        final_video.write_videofile("Aircraft_Complete_Animation.mp4", codec="libx264", fps=24)

    elif ask_merge == "n":
        pass
    else:
        pass