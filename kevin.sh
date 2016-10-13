aaa="null"
while true; do
i=1
vvv=$(ls -tp | grep -v /$ | head -1)

if [ $vvv != $aaa ]; then
	#cp $vvv input.mp4
        #filename=$(../result/result "$i" .mov) 
	../darknet/darknet yolo hack_demo ../darknet/cfg/tiny-yolo.cfg ../darknet/tiny-yolo.weights create2.mp4 ../result/detection_result.mov
	sleep 1
	aaa=$vvv
#       cp ../result/result/temp.mov $filename
        #i=$(( i + 1 ))
else
	echo "waiting new file"
fi

sleep 1
done
