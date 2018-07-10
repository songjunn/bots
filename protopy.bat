@echo off

@set OUT_PATH=%cd%
@set PROTO_PATH=../../service-src/libmessage/proto

cd %PROTO_PATH%

for /f "delims=" %%i in ('dir /b /a-h "*.proto"') do (call protoc.exe -I=./ --python_out=%OUT_PATH%/bots_tyjh/message %%i)

@pause