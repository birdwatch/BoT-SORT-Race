vid_dir="data/videos"
for vid in $vid_dir/*.mp4; do
    echo "Processing $vid"
    .venv/bin/python tools/mc_demo.py video --path $vid -f yolox/exps/example/mot/yolox_x_mix_det.py -c pretrained/bytetrack_x_mot17.pth.tar --with-reid --fp16 --fuse --save_result
done
