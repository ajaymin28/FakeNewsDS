import librosa
import soundfile as sf
import glob
import os
from tqdm import tqdm
from transformers import pipeline
import torch
import json

whisper = pipeline("automatic-speech-recognition", "openai/whisper-large-v3", torch_dtype=torch.float16, device="cuda:0")
whisper.generation_config.language = "english",
whisper.generation_config.forced_decoder_ids = None

def extract_audio_from_video(video_path,audio_save_path):
   audio , sr = librosa.load(video_path)
   sf.write(audio_save_path,audio,sr)


VIDEO_ROOT_PATH = "/home/jbhol/dso/gits/NewsVideoDataset/META_DATA_FILE_PATH"
VIDEOS_LIST = glob.glob(os.path.join(VIDEO_ROOT_PATH,"*.mp4"))

AUDIO_SAVE_PATH_ROOT = "/home/jbhol/dso/gits/NewsVideoDataset/AUDIO_Transcripts"
os.makedirs(AUDIO_SAVE_PATH_ROOT,exist_ok=True)

for video_path in tqdm(VIDEOS_LIST):
   fileroot, filename = os.path.split(video_path)
   filename_wo_ext = filename.split(".mp4")[0]

   AudioFilePath = os.path.join(VIDEO_ROOT_PATH, f"{filename_wo_ext}.wav")

   extract_audio_from_video(video_path,AudioFilePath)

   AudioTranscriptPath = os.path.join(AUDIO_SAVE_PATH_ROOT, f"{filename_wo_ext}_transcript.json")


   transcription = whisper(AudioFilePath, return_timestamps=True)


   with open(AudioTranscriptPath, "w") as f:
      transcription_data = {
         "text": transcription["text"]
      }

      json.dump(transcription_data,f,indent=4)
