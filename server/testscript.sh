#!/bin/bash
curl -d "testData1" -X POST "localhost:5000/files/tf1" -w '%{response_code}' 
sleep 1; echo;
curl -d "testData2" -X POST "localhost:5000/files/tf2" -w '%{response_code}'
sleep 1; echo
curl -d "testData3" -X POST "localhost:5000/files/tf3" -w '%{response_code}' 
sleep 1; echo
curl -X GET "localhost:5000/files" -w '%{response_code}' 
sleep 1; echo
curl -X DELETE "localhost:5000/files/tf1" -w '%{response_code}' 
sleep 1; echo
curl -X GET "localhost:5000/files" -w '%{response_code}'
