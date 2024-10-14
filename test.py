import ollama

system  = '''

Baised on the Transcription user provides with start and end, Highilight the main parts in less then 1 min which can be directly converted into a short. highlight it such that its intresting and also keep the time staps for the clip to start and end. only select a continues Part of the video

Follow this Format and return in valid json 
[{
start: "Start time of the clip",
content: "Highlight Text",
end: "End Time for the highlighted clip"
}]
it should be one continues clip as it will then be cut from the video and uploaded as a tiktok video. so only have one start, end and content

Dont say anything else, just return Proper Json. no explanation etc


IF YOU DONT HAVE ONE start AND end WHICH IS FOR THE LENGTH OF THE ENTIRE HIGHLIGHT, THEN 10 KITTENS WILL DIE, I WILL DO JSON['start'] AND IF IT DOESNT WORK THEN...
'''

User = '''
Das ist ein Test.
'''



def GetHighlight(Transcription):
  print("Getting Highlight from Transcription ") 


  response = ollama.chat(
    model='llama3.2', 
    messages=[
      {"role": "system", "content": system},
      {"role": "user", "content": Transcription + system}
    ]
  )

  print(response['message']['content'])

  json_string = response['message']['content']
  json_string = json_string.replace("json", "")
  json_string = json_string.replace("```", "")
  # print(json_string)
  Start , End = extract_times(json_string)
  if Start == End:
    Ask = input("Error - Get Highlights again (y/n) -> ").lower()
    if Ask == 'y':
      Start , End = GetHighlight(Transcription)
  return Start, End


if __name__ == "__main__":
  print(GetHighlight(User))
