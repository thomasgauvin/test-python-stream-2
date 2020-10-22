from ffmpeg_streaming import Formats, Bitrate, Representation, Size, input

video = input('rtsp://localhost:8554/live');

_480p  = Representation(Size(854, 480), Bitrate(750 * 1024, 192 * 1024))
hls = video.hls(Formats.h264(), hls_list_size=5, hls_time=2)
hls.flags('delete_segments')
hls.representations(_480p)
hls.output('./output/hls1.m3u8')