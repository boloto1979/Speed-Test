import speedtest
import time

st = speedtest.Speedtest()
st.get_best_sever()

st_ping = st.resultes.ping
st_download = round(sr.download() / 1000 / 1000, 1)
st_upload = round(st.upload() / 1000 / 1000, 1)

print(f"Download {st_download}")
print(f"Upload{st_upload}")
print(f"Ping{st_ping}")

#/   python3 speedtxt.py /#
