import sublime, sublime_plugin
import time
import datetime

class mbtimerec(sublime_plugin.TextCommand):
	def run(self, edit):
		time = datetime.datetime.now()
		date = time.strftime( '%d/%m/%Y' )
		
		''' Round to nearest 5 minutes '''
		time = time - datetime.timedelta(minutes=time.minute % 2.5,
									 seconds=time.second,
									 microseconds=time.microsecond)

		discard = datetime.timedelta(minutes=time.minute % 5,
									 seconds=time.second,
									 microseconds=time.microsecond)
		time -= discard
		if discard >= datetime.timedelta(minutes=2.5):
			time += datetime.timedelta(minutes=5)
		
		time = time.strftime('%I:%M%p')
		dt = date + " " + time

		for region in self.view.sel():
			selection = self.view.substr(self.view.line(self.view.sel()[0]))
			if region.empty():
				line = self.view.line(region)
				if line.empty():
					lineRegion = sublime.Region(line.begin(), line.end())
					self.view.replace(edit, line, dt + ' *In progress*')
				elif '*In progress*' in selection:
					startTime = selection[:18] #TODO: make this more robust
					startTime = datetime.datetime.strptime(startTime, '%d/%m/%Y %I:%M%p')
					endTime = date + " " + time
					endTime = datetime.datetime.strptime(endTime, '%d/%m/%Y %I:%M%p')
					timeDiff = endTime - startTime
					timeDiff = "(" + str(timeDiff)[:-3] + ")"
					selection = selection.replace("*In progress*", "- " + time + " " + timeDiff + " ");
					self.view.replace(edit, line, selection)
			else: #Region not empty
				totalHours = 0
				totalMinutes = 0
				
				lines = selection.split('\n')
				for line in lines:
					#Get duration i.e. (10:20)
					duration = (line[28:36]) #This is not strictly necessary..
					#Get hours
					hours = duration[duration.find("(")+1:duration.find(":")]
					minutes = duration[duration.find(":")+1:duration.find(")")]
					
					if hours.isdigit():
						totalHours += int(hours)
				
					if minutes.isdigit():
						totalMinutes += int(minutes)
				
				totalHours += int(totalMinutes / 60)
				totalMinutes = int(totalMinutes % 60)
				if totalMinutes < 10:
					totalMinutes = '0'+str(totalMinutes)
				self.view.insert(edit, self.view.sel()[0].end(), "Total: (" + str(totalHours) + ":" + str(totalMinutes) + ")")


'''

'''



'''
*in progress*
		for region in self.view.sel():  
			# Only interested in empty regions, otherwise they may span multiple  
			# lines, which doesn't make sense for this command.  
			if region.empty():
				# Expand the region to the full line it resides on, excluding the newline  
				line = self.view.line(region)  
				# Extract the string for the line, and add a newline  
				lineContents = self.view.substr(line) + '\n'  
				# Add the text at the beginning of the line  
				self.view.insert(line.begin(), lineContents)  
'''
 

# Extends TextCommand so that run() receives a View to modify.  
'''    def run(self, edit):  
        # Walk through each region in the selection  
        for region in edit.sel():  
            # Only interested in empty regions, otherwise they may span multiple  
            # lines, which doesn't make sense for this command.  
            if region.empty():  
                # Expand the region to the full line it resides on, excluding the newline  
                line = view.line(region)  
                # Extract the string for the line, and add a newline  
                lineContents = view.substr(line) + '\n'  
                # Add the text at the beginning of the line  
                view.insert(line.begin(), lineContents)  
'''
# Simple time recorder Python script in Notepad++
# By Mikey Beck
# Note: Rounds to nearest 5 minutes

#TODO: Total for each day/client - done?
#TODO: Only have one *in progress* per file, don't need to be on same line to use it..maybe?


''' If user has selected text, simply calculate and print total time '''
'''
selected = editor.getSelText()
if selected != "":
	totalHours = 0
	totalMinutes = 0
	
	lines = selected.split('\n')
	for line in lines:
		#Get duration i.e. (10:20)
		duration = (line[28:36]) #This is not strictly necessary..
		#Get hours
		hours = duration[duration.find("(")+1:duration.find(":")]
		minutes = duration[duration.find(":")+1:duration.find(")")]
		
		if hours.isdigit():
			totalHours += int(hours)
	
		if minutes.isdigit():
			totalMinutes += int(minutes)
	
	totalHours += (totalMinutes / 60)
	totalMinutes = (totalMinutes % 60)
	print "Total: (" + str(totalHours) + ":" + str(totalMinutes) + ")"
	
else:

	import time
	import datetime

	line = editor.getCurLine()

	date = time.strftime( '%d/%m/%Y' )
	time = datetime.datetime.now()

	'''''' Round to nearest 5 minutes ''''''
	time = time - datetime.timedelta(minutes=time.minute % 2.5,
								 seconds=time.second,
								 microseconds=time.microsecond)

	discard = datetime.timedelta(minutes=time.minute % 5,
								 seconds=time.second,
								 microseconds=time.microsecond)
	time -= discard
	if discard >= datetime.timedelta(minutes=2.5):
		time += datetime.timedelta(minutes=5)
	
	time = time.strftime('%I:%M%p')



	if '*In progress*' in line:
		currentLineNum  = editor.lineFromPosition(editor.getCurrentPos())
		
		#Get time difference between start & end times
		startTime = line[:18] #TODO: make this more robust
		startTime = datetime.datetime.strptime(startTime, '%d/%m/%Y %I:%M%p')
		endTime = date + " " + time
		endTime = datetime.datetime.strptime(endTime, '%d/%m/%Y %I:%M%p')
		timeDiff = endTime - startTime
		timeDiff = "(" + str(timeDiff)[:-3] + ")"
		
		line = line.replace("*In progress*", "- " + time + " " + timeDiff + " ");
		editor.replaceLine(currentLineNum, line)
		#Go to end of 'current' line	
		EOL = editor.getCurrentPos() + len(editor.getCurLine()) - 2 #This gets the caret to the end of the line, ready to type
		editor.gotoPos(EOL)
	else:
		editor.addText(date + " " + str(time) + " *In progress*")


'''
