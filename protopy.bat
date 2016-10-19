@echo off

@set SRC_DIR=../../server/libmessage/proto

cd %SRC_DIR%

for /f "delims=" %%i in ('dir /b /a-h "*.proto"') do (call protoc.exe -I=./ --python_out=../../../tools/bots/bots_tank/message %%i)

@pause