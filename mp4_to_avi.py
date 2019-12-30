#Convert a video from mp4 to avi format without loss of resolution and frame rate 
import imageio

src_dir = "test2.mp4"
dst_dir = "test2.avi"

reader = imageio.get_reader(src_dir)
fps = reader.get_meta_data()['fps']
writer = imageio.get_writer(dst_dir, fps=fps)

for im in reader:
    writer.append_data(im[:, :, :])
writer.close()
