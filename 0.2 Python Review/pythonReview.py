def create_youtube_video(title,description):
	youtubev={"title":title, "description":description, "likes":0, "dislikes":0,"comments":{}}
	#youtubev["likes"]=495
	return youtubev
def like(youtubev):
	 if "likes" in youtubev:
		youtubev["likes"]+=1
		return youtubev
def dislike(youtubev):
	if "dislikes" in youtubev:
		youtubev["dislikes"]+=1
		return youtubev
def addcomment(youtubev,username,commenttext):
	youtubev["comments"][username]=commenttext
	return youtubev

myVid = create_youtube_video("duck","my duck")
dislike(myVid)
like(myVid)
addcomment(myVid,"Ayala","Yay")
print(myVid)
