headers = {
    # 如果有绿钻，把Cookie放在这里，可以听VIP歌曲
    # SVIP可以听付费歌曲
    "Cookie": "pgv_pvid=122255850; RK=sq2c0WgMkw; ptcz=4b1b3ff0988f8debd6efd3e18dbad03ceafab18b0a393fc9f789aef6a96328f0; fqm_pvqid=a0a0ad77-a339-40c6-8619-1b77f67f1c0a; ts_uid=3130584024; pac_uid=0_ac24f3eb1dcfc; iip=0; _qimei_uuid42=1810314123a1005f0d0cef1d43a703bb45efc6d070; _qimei_q36=; _qimei_h38=19c58f6f0d0cef1d43a703bb0200000db18103; qq_domain_video_guid_verify=41efdef0db834ab5; _qimei_fingerprint=dee340132eb2aa6ba02de0f5902c82e2; suid=0_ac24f3eb1dcfc; _clck=3926629569|1|fqd|0; fqm_sessionid=498ac034-b60c-48ee-919a-6422f63f576d; pgv_info=ssid=s6619484056; ts_refer=www.bing.com/; _qpsvr_localtk=0.6034994123552242; login_type=2; psrf_qqaccess_token=; psrf_qqrefresh_token=; qqmusic_key=W_X_63B0azhTA2-qY_rA0dGK2bhLIm8WobpyjsAAPbEYfwX3Qf-z1VP4vOrndhRTaxi80M1IDCOesSsFDmEmkh-TeZhq7_2U; psrf_qqopenid=; euin=oK6kowEAoK4z7Kn57KoANKnqon**; wxopenid=opCFJw5RhNkFU_yoeFSYkmip3qkY; psrf_qqunionid=; qm_keyst=W_X_63B0azhTA2-qY_rA0dGK2bhLIm8WobpyjsAAPbEYfwX3Qf-z1VP4vOrndhRTaxi80M1IDCOesSsFDmEmkh-TeZhq7_2U; wxuin=1152921505015329090; wxunionid=oqFLxshjv_Ya8QI5BkR4WR487Vn0; wxrefresh_token=85_0h-R2oLVep15CJmwIeZzPWMwkV10cn6mPkDsPRwvxmvUtWUMd2GYGpnx2-5hfzXUSEoTU2uQXTeBlABWUmNL0AAHyWZlOK9UMglB40wp5uk; qm_keyst=W_X_63B0azhTA2-qY_rA0dGK2bhLIm8WobpyjsAAPbEYfwX3Qf-z1VP4vOrndhRTaxi80M1IDCOesSsFDmEmkh-TeZhq7_2U; tmeLoginType=1; wxuin=1152921505015329090; ts_last=y.qq.com/n/ryqq/player"
}

api = {
    "search": "https://c.y.qq.com/soso/fcgi-bin/music_search_new_platform?format=json&w={}&n={}",
    "get_album_picture": "http://imgcache.qq.com/music/photo/album_300/{}/300_albumpic_{}_0.jpg",
    "get_songmid": "https://c.y.qq.com/v8/fcg-bin/fcg_play_single_song.fcg?songid={}&tpl=yqq_song_detail&format=json",
    "get_song_url": "https://u6.y.qq.com/cgi-bin/musics.fcg?_=1730450550757&sign={}",
    "play_on": "https://ws6.stream.qqmusic.qq.com/"
}
