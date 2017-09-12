#!/usr/bin/env python
import os
import os.path
import sys
import json

if len(sys.argv) < 2:
	sys.exit()

# Pull values off of command line
pystDir = sys.argv[1]
shitHeapFile = sys.argv[2]

# Create an empty shit heap
shitHeap = {
	"assets": {
		"actors": {},
		"scenes": {},
		"skins": {}
	},
	"layout": {
		"textbox": {},
		"actors": {}
	},
	"pystScript": "",
	"jystScript": ""
}

# Process actors
print "ACTORS:"
for root, subdirs, files in os.walk(pystDir + "/assets/actors"):
	for subdir in subdirs:
		actor = shitHeap["assets"]["actors"][subdir] = {
			"moods": {}
		}
		for root2, subdirs2, files2 in os.walk(root + "/" + subdir):
			for file in files2:
				if file == ".DS_Store":
					continue
				print "\t" + file

				extension = os.path.splitext(file)[1]

				with open(root2 + "/" + file, 'rb') as actorImage:
					actor["moods"][file.split(".")[0]] = {
						"image": actorImage.read().encode('base64').rstrip(),
						"mimeType": "image/" + extension[1:]
					}

# Process scenes
print "SCENES:"
for root, subdirs, files in os.walk(pystDir + "/assets/scenes"):
	for subdir in subdirs:
		scene = shitHeap["assets"]["scenes"][subdir] = {
			"variants": {}
		}
		for root2, subdirs2, files2 in os.walk(root + "/" + subdir):
			for file in files2:
				if file == ".DS_Store":
					continue
				print "\t" + file 

				extension = os.path.splitext(file)[1]

				with open(root2 + "/" + file, 'rb') as sceneImage:
					scene["variants"][file.split(".")[0]] = {
						"image": sceneImage.read().encode('base64').rstrip(),
						"mimeType": "image/" + extension[1:]
					}

# Process skins
print "SKINS:"
for root, subdirs, files in os.walk(pystDir + "/assets/skins"):
	for subdir in subdirs:
		skin = shitHeap["assets"]["skins"][subdir] = {
			"variants": {}
		}
		for root2, subdirs2, files2 in os.walk(root + "/" + subdir):
			for file in files2:
				if file == ".DS_Store":
					continue

				print "\t" + file

				extension = os.path.splitext(file)[1]

				with open(root2 + "/" + file, 'rb') as skinImage:
					skin["variants"][file.split(".")[0]] = {
						"image": skinImage.read().encode('base64').rstrip(),
						"mimeType": "image/" + extension[1:]
					}

# Add layout
with open(pystDir + "/game.layout", 'r') as f:
	shitHeap["layout"] = json.load(f)

# Add script
with open(pystDir + "/game.pyst", 'r') as f:
	shitHeap["pystScript"] = f.read().encode('base64').rstrip()

# Add script
with open(pystDir + "/game.jyst", 'r') as f:
	shitHeap["jystScript"] = f.read().encode('base64').rstrip()

# Dump shit heap
with open(shitHeapFile, 'w') as f:
	json.dump(shitHeap, f, sort_keys=True, indent=4, separators=(',', ': '))
