# -*- mode: python -*-
{
    "targets": [{
        "target_name": "v4l2camera", 
        "sources": ["capture.c", "v4l2camera.cc"],
        "include_dirs" : [
 	    "<!(node -e \"require('nan')\")"
	],
        "cflags": ["-Wall", "-Wextra", "-pedantic", "-O3"],
        "xcode_settings": {
    	    "OTHER_CPLUSPLUSFLAGS": [],
        },
        "cflags_c": ["-Wunused-parameter"], 
        "cflags_cc": []
    }]
}

