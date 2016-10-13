while true; do
vvv=$(ls -tp | grep -v /$ | head -1)
cp $vvv class4,mp4
cp 
if [ ! -f /home/carhack/video/class4.mp4 ]; then
    echo "File not found!"
#   ./darknet/darknet yolo hack_demo ./darknet/cfg/tiny-yolo.cfg ./darknet/tiny-yolo.weights /home/carhack/video/tester1.mp4 ./result/test.mov
 
else
    echo "exist"
   ./darknet/darknet yolo hack_demo ./darknet/cfg/tiny-yolo.cfg ./darknet/tiny-yolo.weights /home/carhack/video/class4.mp4 ./result/test.mov

   ffmpeg -i ./result/test.mov -vcodec copy -acodec copy ./result/test.mp4
 
fi
sleep 1
done
