.PHONY: build clean build-addon build-movie build-serie build-anime build-subs build-exec build-bonus

build-movie:
	#Directory, File: Default Test (BlueRay)
	mkdir -p ~/python-multimedia-filemapper/test-library/'Sisters.And.Brothers.2011.1080p.BluRay.H264.AAC-RARBG'
	touch ~/python-multimedia-filemapper/test-library/'Sisters.And.Brothers.2011.1080p.BluRay.H264.AAC-RARBG'/'Sisters.And.Brothers.2011.1080p.BluRay.H264.AAC-RARBG.mkv'
	
	#Directory, File: Default Test
	mkdir -p ~/python-multimedia-filemapper/test-library/'Innocent.Bystanders.1972.BRRip.XviD.MP3-RARBG'
	touch ~/python-multimedia-filemapper/test-library/'Innocent.Bystanders.1972.BRRip.XviD.MP3-RARBG'/'Innocent.Bystanders.1972.BRRip.XviD.MP3-RARBG.mkv'
	
	#Directory, File: Default Test (Dates)
	mkdir -p ~/python-multimedia-filemapper/test-library/'Meet.Him.And.Die.1976.1080p.BluRay.H264.AAC-RARBG'
	touch ~/python-multimedia-filemapper/test-library/'Meet.Him.And.Die.1976.1080p.BluRay.H264.AAC-RARBG'/'Meet.Him.And.Die.1976.1080p.BluRay.H264.AAC-RARBG.mkv'
	
	#Directory, Subdirectory, File: Default Test (Mp3)
	mkdir -p ~/python-multimedia-filemapper/test-library/'Littlerock.2010.BRRip.XviD.MP3-RARBG'
	mkdir -p ~/python-multimedia-filemapper/test-library/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'Littlerock.2010(subtitle)'
	touch ~/python-multimedia-filemapper/test-library/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'Littlerock.2010(subtitle)'/'Littlerock.2010(english).srt'
	touch ~/python-multimedia-filemapper/test-library/'Littlerock.2010.BRRip.XviD.MP3-RARBG'/'Littlerock.2010.BRRip.XviD.MP3-RARBG.mkv'
	
	#Directory, Subdirectory, File: Default Test (EXTENDED.CUT,BRRip, XviD)
	mkdir -p ~/python-multimedia-filemapper/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'
	mkdir -p ~/python-multimedia-filemapper/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Were.the.Millers.2013.(subtitle)'
	touch ~/python-multimedia-filemapper/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Were.the.Millers.2013.(subtitle)'/'Were.the.Millers.2013(english).srt'
	touch ~/python-multimedia-filemapper/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'System.nfo'
	touch ~/python-multimedia-filemapper/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Readme.txt'
	touch ~/python-multimedia-filemapper/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'RARBG.com'
	touch ~/python-multimedia-filemapper/test-library/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG'/'Were.the.Millers.2013.EXTENDED.CUT.BRRip.XviD.MP3-RARBG.mkv'

	#Directory, File: Unkonw Movie
	#mkdir -p ~/python-multimedia-filemapper/test-library/'Lost.Kiddo.The.Movie.(1080p).(2015)'
	#touch ~/python-multimedia-filemapper/test-library/'Lost.Kiddo.The.Movie.(1080p).(2015)'/'Lost.Kiddo.The.Movie.(1080p).(2015).mkv'

build-serie:
	#Directory, File: Default Test
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game Of Thrones'
	mkdir -p ~/python-multimedia-filemapper/test-library/'WestWorld'
	mkdir -p ~/python-multimedia-filemapper/test-library/'WestWorld.S01E02.1080p'
	touch ~/python-multimedia-filemapper/test-library/'WestWorld.S01E02.1080p'/'WestWorld.S01E02.1080p.mkv'
	
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'Game.of.Thrones.S06E01.1080p.BluRay.x264-ROVERS[rartv].mkv'
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'Game.of.Thrones.S06E02.1080p.BluRay.x264-ROVERS[rartv].mkv'
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'Game.of.Thrones.S06E03.1080p.BluRay.x264-ROVERS[rartv].mkv'
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'system.nfo'
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'system.txt'
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones.S06.1080p.BluRay.x264-ROVERS[rartv]'/'system.com'
	
	#Directory, Subdirectory, File: Default Test
	#mkdir -p ~/python-multimedia-filemapper/test-library/'Game.of.Thrones-season2'/
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game.of.Thrones.season-3'/
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game.of.Thrones [Season 1]'/
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E01.1080p.mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E02.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E02.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E02.1080p.mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E03.1080p.mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E03.subtitles'
	touch ~/python-multimedia-filemapper/test-library/'Game.of.Thrones [Season 1]'/'Game.Of.Thrones.S01E03.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E03.subtitles'/'Game.Of.Thrones.s01e03(english).srt'
	
	#Directory, File: Retrieving Lost Episode Test
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/python-multimedia-filemapper/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E05.1080p.mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E05.subtitles'
	touch ~/python-multimedia-filemapper/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E05.subtitles'/'Game.Of.Thrones.S01E05(english).srt'
	touch ~/python-multimedia-filemapper/test-library/'Game.Of.Thrones.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E05.subtitles'/'Game.Of.Thrones.S01E05(es).srt'
	
	#Directory, File: Default
	mkdir -p ~/python-multimedia-filemapper/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/
	touch ~/python-multimedia-filemapper/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Teen.Wolf.S01E05.1080p.mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Teen.Wolf.S01E05.subtitles'
	touch ~/python-multimedia-filemapper/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Teen.Wolf.S01E05.subtitles'/'Teen.Wolf.S01E05(english).srt'
	touch ~/python-multimedia-filemapper/test-library/'Teen.Wolf.S01E05.1080p.BluRay.x265-PODO[rartv]'/'Teen.Wolf.S01E05.subtitles'/'Teen.Wolf.S01E05(es).srt'
	
	#Directory, File: Retrieving Repetead Lost Episode Test
	#mkdir -p ~/python-multimedia-filemapper/test-library/'Game.Of.Thrones.S01E01.1080p.BluRay.x265-PODO[rartv]'/'Game.Of.Thrones.S01E01.1080p.mkv'
	
	#Directory, Subdirectory, File: Unkonwn Show
	#mkdir -p ~/python-multimedia-filemapper/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'
	#touch ~/python-multimedia-filemapper/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'System.nfo'
	#touch ~/python-multimedia-filemapper/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'rartv.txt'
	#mkdir -p ~/python-multimedia-filemapper/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'sub'
	#touch ~/python-multimedia-filemapper/test-library/'Krystal-The.Black Stripper-S02E01-The.dAy.0f.7he stripper.720p[rartv]'/'sub'/'Krystal-The.Black Stripper-S02E01(es).srt'

build-anime:
	mkdir -p ~/python-multimedia-filemapper/test-library/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/
	touch ~/python-multimedia-filemapper/test-library/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B].mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/'[PuyaSubs!] Yuri!!! On ICE - 11 subtitle'/
	touch ~/python-multimedia-filemapper/test-library/'[PuyaSubs!] Yuri!!! On ICE - 11 [720p][663F641B]'/'[PuyaSubs!] Yuri!!! On ICE - 11 subtitle'/'[PuyaSubs!] Yuri!!! On ICE - 11(spanish).srt'
	
	mkdir -p ~/python-multimedia-filemapper/test-library/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/
	touch ~/python-multimedia-filemapper/test-library/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286].mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/'[Krosis] Getsuyoubi no Tawawa - 10 subtitle'/
	touch ~/python-multimedia-filemapper/test-library/'[Krosis] Getsuyoubi no Tawawa - 10 [1E0FA286]'/'[Krosis] Getsuyoubi no Tawawa - 10 subtitle'/'[Krosis] Getsuyoubi no Tawawa - 10(eng).srt'
	
	mkdir -p ~/python-multimedia-filemapper/test-library/'[HorribleSubs] One Piece - 768 [1080p]'/
	touch ~/python-multimedia-filemapper/test-library/'[HorribleSubs] One Piece - 768 [1080p]'/'[HorribleSubs] One Piece - 768 [1080p].mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'[HorribleSubs] One Piece - 768 [1080p]'/'[HorribleSubs] One Piece - 768 subtitle'/
	touch ~/python-multimedia-filemapper/test-library/'[HorribleSubs] One Piece - 768 [1080p]'/'[HorribleSubs] One Piece - 768 subtitle'/'[HorribleSubs] One Piece - 768(eng).srt'
	
	mkdir -p ~/python-multimedia-filemapper/test-library/'[HorribleSubs] One Piece x769 [1080p]'/
	touch ~/python-multimedia-filemapper/test-library/'[HorribleSubs] One Piece x769 [1080p]'/'[HorribleSubs] One Piece x769 [1080p].mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'[HorribleSubs] One Piece x769 [1080p]'/'[HorribleSubs] One Piece x769 subtitle'/
	touch ~/python-multimedia-filemapper/test-library/'[HorribleSubs] One Piece x769 [1080p]'/'[HorribleSubs] One Piece x769 subtitle'/'[HorribleSubs] One Piece x769(eng).srt'
	
	mkdir -p ~/python-multimedia-filemapper/test-library/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/
	touch ~/python-multimedia-filemapper/test-library/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC).mp4'
	mkdir -p ~/python-multimedia-filemapper/test-library/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/'[Ohys-Raws] Detective Conan - 842 subtitle'/
	touch ~/python-multimedia-filemapper/test-library/'[Ohys-Raws] Detective Conan - 842 (NTV 1280x720 x264 AAC)'/'[Ohys-Raws] Detective Conan - 842 subtitle'/'[Ohys-Raws] Detective Conan - 842(eng).srt'
	
	#CASO PARTICULAR DEL PUTO ANIME con Episode
	mkdir -p ~/python-multimedia-filemapper/test-library/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/
	touch ~/python-multimedia-filemapper/test-library/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p].mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/'[Dcms-Fansubs] Detective Conan Episode 840 subtitle'/
	touch ~/python-multimedia-filemapper/test-library/'[Dcms-Fansubs] Detective Conan Episode 840 [1080p]'/'[Dcms-Fansubs] Detective Conan Episode 840 subtitle'/'[Dcms-Fansubs] Detective Conan Episode 840(eng).srt'
	
	#Number on name
	mkdir -p ~/python-multimedia-filemapper/test-library/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/
	touch ~/python-multimedia-filemapper/test-library/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/'[HorribleSubs] Mob Psycho 100 - 12 [1080p].mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/'[HorribleSubs] Mob Psycho 100 - 12 subs'/
	touch ~/python-multimedia-filemapper/test-library/'[HorribleSubs] Mob Psycho 100 - 12 [1080p]'/'[HorribleSubs] Mob Psycho 100 - 12 subs'/'[HorribleSubs] Mob Psycho 100 - 12 (eng).srt'

build-subs:
	cp -ar ~/python-multimedia-filemapper/subs ~/python-multimedia-filemapper/test-library/

build-bonus:
	mkdir -p ~/python-multimedia-filemapper/test-library/'Howls_Moving_Castle_(2004)_[720p,HDTV,x264,DTS]-FlexGet'
	touch ~/python-multimedia-filemapper/test-library/'Howls_Moving_Castle_(2004)_[720p,HDTV,x264,DTS]-FlexGet'/'Howls_Moving_Castle_(2004)_[720p,HDTV,x264,DTS]-FlexGet.mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'Battle Royale (Batoru.Rowaiaru) (2000)'
	touch ~/python-multimedia-filemapper/test-library/'Battle Royale (Batoru.Rowaiaru) (2000)'/'Battle.Royale.(Batoru.Rowaiaru).(2000).(Special.Edition).CD1of2.DVDRiP.XviD-[ZeaL].mkv'
	mkdir -p ~/python-multimedia-filemapper/test-library/'Un Espia y Medio (2016) [MicroHD 1080p][AC3 5.1-DTS 5.1-Castellano-AC3 5.1 Ingles+Subs][ES-EN]'
	touch ~/python-multimedia-filemapper/test-library/'Un Espia y Medio (2016) [MicroHD 1080p][AC3 5.1-DTS 5.1-Castellano-AC3 5.1 Ingles+Subs][ES-EN]'/'Un Espia y Medio (2016) [MicroHD 1080p][AC3 5.1-DTS 5.1-Castellano-AC3 5.1 Ingles+Subs][ES-EN].mkv'


build-addon:
	rm -f ~/python-multimedia-filemapper/trunk/addon/'script.galung.project.zip'
	zip -r ~/python-multimedia-filemapper/trunk/addon/'script.galung.project.zip' ~/TFG/trunk/addon/script.galung.project/


build-all:
	make build-movie
	make build-serie
	make build-anime

build-exec:
	make clean
	make build-all
	./main.py

clean:
	rm -rf ~/python-multimedia-filemapper/test-library/*
	rm -rf ~/python-multimedia-filemapper/result/*
