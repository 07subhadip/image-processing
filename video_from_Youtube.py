import cv2
import pytube

try:
    # Video downloading with error handling
    url = "https://www.youtube.com/watch?v=wOOOiwxvIhw"
    yt = pytube.YouTube(url)
    ys = yt.streams.get_highest_resolution()  # Or choose a different stream as needed
    video_path = "video.mp4"
    ys.download(filename=video_path)

    # Video capture and processing with resource management
    cap = cv2.VideoCapture(video_path)
    if cap.isOpened():
        fourcc = cv2.VideoWriter_fourcc(*"XVID")

        # Optional video writing configuration (adjust resolution and quality if needed)
        output = cv2.VideoWriter(
            "Sukuna_Edit.avi", fourcc, 20.0, (640, 480)
        )

        while True:
            ret, frame = cap.read()
            if ret:
                # Implement video editing operations here (replace with your logic)
                # Example: adding text using OpenCV
                cv2.putText(
                    frame,
                    "Your Edited Text",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 255, 0),
                    2,
                )

                cv2.imshow("Sukuna Edit", frame)

                # Write edited frame to output video (if desired)
                output.write(frame)
                k = cv2.waitKey(25)
                if k==True & 0xFF == ord("q"):
                    break
            else:
                break

        # Explicit release for older OpenCV versions
        cap.release()

        # Close output video writer if used
        if output:
            output.release()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    cv2.destroyAllWindows()
    print("Done")
