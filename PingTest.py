from speedtest import Speedtest

st = Speedtest()

speed_download = st.download()
speed_upload = st.upload()
st.get_servers([])
ping = st.results.ping

print("Download: ", speed_download)
print("Upload: ", speed_upload)
print("Ping: ", ping)

if speed_download > 5000000.00 and speed_upload > 3500000.00 and ping < 60:
    print("You have a nice internet connection speed!")
else:
    print("Hm, it's lower than always. Check parameters.")