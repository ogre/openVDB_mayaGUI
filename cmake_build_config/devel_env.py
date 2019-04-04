#!/usr/bin/env python

if __name__ == '__main__':
	try:
		import os, sys
		sys.path.append('//bbcfg/pkgs/prod/bbenv/2018_10_02_51acfccf97ba')
		import bbenv

		cfg_file = os.path.dirname(sys.argv[0]).replace('\\', '/') + "/cfg_devel_env"
		cfg_file += '_' + bbenv.OS()
		print cfg_file

		project_env = bbenv.GetFromFile_OsEnv( cfg_file )
		bbenv.SetEnv( project_env )
		curr_dir = os.path.dirname( cfg_file )
		if (bbenv.OS() == "nt64"):	os.system('powershell -NoExit -Command "cd %s" ' % curr_dir)
		else:						os.system("$SHELL")
	except:
		import traceback
		print traceback.format_exc()
		#os.system("pause")
