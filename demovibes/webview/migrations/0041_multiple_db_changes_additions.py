
from south.db import db
from django.db import models
from demovibes.webview.models import *

class Migration:
    
    def forwards(self, orm):
        
        # Adding model 'Faq'
        db.create_table('webview_faq', (
            ('added', models.DateTimeField(auto_now_add=True, db_index=True)),
            ('last_updated', models.DateTimeField(null=True, editable=False, blank=True)),
            ('question', models.CharField(max_length=500, verbose_name="Question")),
            ('priority', models.IntegerField(default=0, null=True, blank=True)),
            ('active', models.BooleanField(default=True, verbose_name="Active?", db_index=True)),
            ('answer', models.TextField(verbose_name="Answer")),
            ('id', models.AutoField(primary_key=True)),
            ('added_by', models.ForeignKey(orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal('webview', ['Faq'])
        
        # Adding model 'Screenshot'
        db.create_table('webview_screenshot', (
            ('startswith', models.CharField(max_length=1, editable=False, db_index=True)),
            ('last_updated', models.DateTimeField(null=True, editable=False, blank=True)),
            ('description', models.TextField(verbose_name="Description")),
            ('image', models.ImageField(null=True, upload_to='media/screenshot/image', blank=True)),
            ('active', models.BooleanField(default=True, verbose_name="Active?", db_index=True)),
            ('id', models.AutoField(primary_key=True)),
            ('added_by', models.ForeignKey(orm['auth.User'], related_name="screenshoit_addedby", null=True, blank=True)),
            ('name', models.CharField(max_length=70, unique=True, verbose_name="Screen Name")),
        ))
        db.send_create_signal('webview', ['Screenshot'])
        
        # Adding field 'SongType.symbol'
        db.add_column('webview_songtype', 'symbol', models.ImageField(null=True, upload_to='media/songsource/symbol', blank=True))
        
        # Adding field 'ArtistVote.rating'
        db.add_column('webview_artistvote', 'rating', models.CharField(default='U', max_length=1))
        
        # Adding field 'ArtistVote.comment'
        db.add_column('webview_artistvote', 'comment', models.CharField(max_length=250, verbose_name="Comment"))
        
        # Adding field 'News.last_updated'
        db.add_column('webview_news', 'last_updated', models.DateTimeField(null=True, editable=False, blank=True))
        
        # Adding field 'Song.al_id'
        db.add_column('webview_song', 'al_id', models.IntegerField(null=True, verbose_name="Atari Legends ID", blank=True))
        
        # Adding field 'Link.last_updated'
        db.add_column('webview_link', 'last_updated', models.DateTimeField(null=True, editable=False, blank=True))
        
        # Adding field 'Song.dtv_id'
        db.add_column('webview_song', 'dtv_id', models.IntegerField(null=True, verbose_name="Demoscene.TV", blank=True))
        
        # Adding field 'SongType.image'
        db.add_column('webview_songtype', 'image', models.ImageField(null=True, upload_to='media/songsource/image', blank=True))
        
        # Adding field 'Song.explicit'
        db.add_column('webview_song', 'explicit', models.BooleanField(default=False, verbose_name="Explicit Lyrics?"))
        
        # Deleting field 'ArtistVote.vote'
        db.delete_column('webview_artistvote', 'vote')
        
        # Changing field 'RadioStream.name'
        db.alter_column('webview_radiostream', 'name', models.CharField(max_length=120, verbose_name="Stream Name"))
        
        # Changing field 'RadioStream.url'
        db.alter_column('webview_radiostream', 'url', models.CharField(max_length=120, verbose_name="Direct URL"))
        
        # Changing field 'RadioStream.country_code'
        db.alter_column('webview_radiostream', 'country_code', models.CharField(max_length=10, verbose_name="Country Code"))
        
        # Changing field 'Group.last_updated'
        db.alter_column('webview_group', 'last_updated', models.DateTimeField(null=True, editable=False, blank=True))
        
        # Changing field 'Group.name'
        db.alter_column('webview_group', 'name', models.CharField(unique=True, max_length=80, verbose_name="* Name", db_index=True))
        
        # Changing field 'Song.pouetid'
        db.alter_column('webview_song', 'pouetid', models.IntegerField(null=True, verbose_name="Pouet ID", blank=True))
        
        # Changing field 'Link.status'
        db.alter_column('webview_link', 'status', models.CharField(default='A', max_length=1, db_index=True))
        
        # Changing field 'Artist.last_updated'
        db.alter_column('webview_artist', 'last_updated', models.DateTimeField(null=True, editable=False, blank=True))
        
        # Changing field 'Label.last_updated'
        db.alter_column('webview_label', 'last_updated', models.DateTimeField(null=True, editable=False, blank=True))
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Faq'
        db.delete_table('webview_faq')
        
        # Deleting model 'Screenshot'
        db.delete_table('webview_screenshot')
        
        # Deleting field 'SongType.symbol'
        db.delete_column('webview_songtype', 'symbol')
        
        # Deleting field 'ArtistVote.rating'
        db.delete_column('webview_artistvote', 'rating')
        
        # Deleting field 'ArtistVote.comment'
        db.delete_column('webview_artistvote', 'comment')
        
        # Deleting field 'News.last_updated'
        db.delete_column('webview_news', 'last_updated')
        
        # Deleting field 'Song.al_id'
        db.delete_column('webview_song', 'al_id')
        
        # Deleting field 'Link.last_updated'
        db.delete_column('webview_link', 'last_updated')
        
        # Deleting field 'Song.dtv_id'
        db.delete_column('webview_song', 'dtv_id')
        
        # Deleting field 'SongType.image'
        db.delete_column('webview_songtype', 'image')
        
        # Deleting field 'Song.explicit'
        db.delete_column('webview_song', 'explicit')
        
        # Adding field 'ArtistVote.vote'
        db.add_column('webview_artistvote', 'vote', models.IntegerField(default=0))
        
        # Changing field 'RadioStream.name'
        db.alter_column('webview_radiostream', 'name', models.CharField(max_length=120))
        
        # Changing field 'RadioStream.url'
        db.alter_column('webview_radiostream', 'url', models.CharField(max_length=120))
        
        # Changing field 'RadioStream.country_code'
        db.alter_column('webview_radiostream', 'country_code', models.CharField(max_length=10))
        
        # Changing field 'Group.last_updated'
        db.alter_column('webview_group', 'last_updated', models.DateTimeField(null=True, blank=True))
        
        # Changing field 'Group.name'
        db.alter_column('webview_group', 'name', models.CharField(max_length=30, unique=True, verbose_name="* Name", db_index=True))
        
        # Changing field 'Song.pouetid'
        db.alter_column('webview_song', 'pouetid', models.IntegerField(null=True, blank=True))
        
        # Changing field 'Link.status'
        db.alter_column('webview_link', 'status', models.CharField(default='A', max_length=1))
        
        # Changing field 'Artist.last_updated'
        db.alter_column('webview_artist', 'last_updated', models.DateTimeField(null=True, blank=True))
        
        # Changing field 'Label.last_updated'
        db.alter_column('webview_label', 'last_updated', models.DateTimeField(null=True, blank=True))
        
    
    
    models = {
        'webview.theme': {
            'css': ('models.CharField', [], {'max_length': '120'}),
            'description': ('models.TextField', [], {'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'preview': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/theme_preview'", 'blank': 'True'}),
            'title': ('models.CharField', [], {'max_length': '20'})
        },
        'webview.news': {
            'Meta': {'ordering': "['-added']"},
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True'}),
            'icon': ('models.URLField', [], {'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'}),
            'status': ('models.CharField', [], {'max_length': '1'}),
            'text': ('models.TextField', [], {}),
            'title': ('models.CharField', [], {'max_length': '100'})
        },
        'webview.songtype': {
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/songsource/image'", 'blank': 'True'}),
            'symbol': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/songsource/symbol'", 'blank': 'True'}),
            'title': ('models.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'webview.radiostream': {
            'active': ('models.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'bitrate': ('models.IntegerField', [], {}),
            'country_code': ('models.CharField', [], {'max_length': '10', 'verbose_name': '"Country Code"'}),
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '120', 'verbose_name': '"Stream Name"'}),
            'streamtype': ('models.CharField', [], {'max_length': '1'}),
            'url': ('models.CharField', [], {'max_length': '120', 'verbose_name': '"Direct URL"'})
        },
        'webview.countrylist': {
            'Meta': {'ordering': "['name']"},
            'code': ('models.CharField', [], {'max_length': '20'}),
            'flag': ('models.CharField', [], {'max_length': '20'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'name': ('models.CharField', [], {'max_length': '60'})
        },
        'webview.group': {
            'Meta': {'ordering': "['name']"},
            'created_by': ('models.ForeignKey', ['User'], {'related_name': '"group_createdby"', 'null': 'True', 'blank': 'True'}),
            'found_date': ('models.DateField', [], {'null': 'True', 'verbose_name': '"Found Date"', 'blank': 'True'}),
            'group_icon': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/groups/icons'", 'blank': 'True'}),
            'group_logo': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/groups'", 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'info': ('models.TextField', [], {'verbose_name': '"Group Info"', 'blank': 'True'}),
            'last_updated': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'}),
            'name': ('models.CharField', [], {'unique': 'True', 'max_length': '80', 'verbose_name': '"* Name"', 'db_index': 'True'}),
            'pouetid': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Pouet ID"', 'blank': 'True'}),
            'startswith': ('models.CharField', [], {'max_length': '1', 'editable': 'False', 'db_index': 'True'}),
            'status': ('models.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'webpage': ('models.URLField', [], {'verbose_name': '"Website"', 'blank': 'True'}),
            'wiki_link': ('models.URLField', [], {'blank': 'True'})
        },
        'webview.song': {
            'Meta': {'ordering': "['title']"},
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'al_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Atari Legends ID"', 'blank': 'True'}),
            'artists': ('models.ManyToManyField', ['Artist'], {'null': 'True', 'blank': 'True'}),
            'bitrate': ('models.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'cvgm_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"CVGM SongID"', 'blank': 'True'}),
            'dtv_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Demoscene.TV"', 'blank': 'True'}),
            'explicit': ('models.BooleanField', [], {'default': 'False', 'verbose_name': '"Explicit Lyrics?"'}),
            'file': ('models.FileField', [], {'verbose_name': '"File"', 'upload_to': "'media/music'"}),
            'groups': ('models.ManyToManyField', ['Group'], {'null': 'True', 'blank': 'True'}),
            'hol_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"H.O.L. ID"', 'blank': 'True'}),
            'hvsc_url': ('models.URLField', [], {'verbose_name': '"HVSC Link"', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'info': ('models.TextField', [], {'blank': 'True'}),
            'labels': ('models.ManyToManyField', ['Label'], {'null': 'True', 'blank': 'True'}),
            'last_changed': ('models.DateTimeField', [], {'auto_now': 'True'}),
            'lemon_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Lemon64 ID"', 'blank': 'True'}),
            'locked_until': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'necta_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Necta SongID"', 'blank': 'True'}),
            'num_favorited': ('models.IntegerField', [], {'default': '0'}),
            'platform': ('models.ForeignKey', ['SongPlatform'], {'null': 'True', 'blank': 'True'}),
            'pouetid': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Pouet ID"', 'blank': 'True'}),
            'projecttwosix_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Project2612 ID"', 'blank': 'True'}),
            'rating': ('models.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rating_total': ('models.IntegerField', [], {'default': '0'}),
            'rating_votes': ('models.IntegerField', [], {'default': '0'}),
            'release_year': ('models.CharField', [], {'max_length': '"4"', 'blank': 'True', 'null': 'True', 'verbose_name': '"Release Year"', 'db_index': 'True'}),
            'remix_of_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Mix SongID"', 'blank': 'True'}),
            'samplerate': ('models.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'song_length': ('models.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'startswith': ('models.CharField', [], {'max_length': '1', 'editable': 'False', 'db_index': 'True'}),
            'status': ('models.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'times_played': ('models.IntegerField', [], {'default': '0', 'null': 'True'}),
            'title': ('models.CharField', [], {'max_length': '80', 'verbose_name': '"* Song Name"', 'db_index': 'True'}),
            'type': ('models.ForeignKey', ['SongType'], {'null': 'True', 'verbose_name': "'Source'", 'blank': 'True'}),
            'uploader': ('models.ForeignKey', ['User'], {'null': 'True', 'blank': 'True'}),
            'wos_id': ('models.CharField', [], {'verbose_name': '"W.O.S. ID"', 'max_length': '8', 'null': 'True', 'blank': 'True'}),
            'zxdemo_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"ZXDemo ID"', 'blank': 'True'})
        },
        'webview.privatemessage': {
            'Meta': {'ordering': "['-sent']"},
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'message': ('models.TextField', [], {}),
            'reply_to': ('models.ForeignKey', ["'PrivateMessage'"], {'default': 'None', 'null': 'True', 'blank': 'True'}),
            'sender': ('models.ForeignKey', ['User'], {'related_name': '"sent_messages"'}),
            'sent': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'subject': ('models.CharField', [], {'max_length': '60'}),
            'to': ('models.ForeignKey', ['User'], {}),
            'unread': ('models.BooleanField', [], {'default': 'True'}),
            'visible': ('models.BooleanField', [], {'default': 'True', 'db_index': 'True'})
        },
        'webview.compilation': {
            'Meta': {'ordering': "['name']"},
            'bar_code': ('models.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'comp_icon': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/compilations/icons'", 'blank': 'True'}),
            'cover_art': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/compilations'", 'blank': 'True'}),
            'created_by': ('models.ForeignKey', ['User'], {'null': 'True', 'blank': 'True'}),
            'date_added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'details_page': ('models.URLField', [], {'blank': 'True'}),
            'download_link': ('models.URLField', [], {'blank': 'True'}),
            'hol_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"H.O.L. ID"', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'info': ('models.TextField', [], {'blank': 'True'}),
            'label': ('models.CharField', [], {'max_length': '30', 'verbose_name': '"Prod. Label"', 'blank': 'True'}),
            'last_updated': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'media_format': ('models.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'name': ('models.CharField', [], {'unique': 'True', 'max_length': '30', 'verbose_name': '"* Name"', 'db_index': 'True'}),
            'num_discs': ('models.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pouet': ('models.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'prod_artists': ('models.ManyToManyField', ['Artist'], {'null': 'True', 'verbose_name': '"Production Artists"', 'blank': 'True'}),
            'prod_groups': ('models.ManyToManyField', ['Group'], {'null': 'True', 'verbose_name': '"Production Groups"', 'blank': 'True'}),
            'prod_notes': ('models.TextField', [], {'blank': 'True'}),
            'projecttwosix_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Project2612 ID"', 'blank': 'True'}),
            'purchase_page': ('models.URLField', [], {'blank': 'True'}),
            'rel_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'running_time': ('models.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'songs': ('models.ManyToManyField', ['Song'], {'null': 'True', 'blank': 'True'}),
            'startswith': ('models.CharField', [], {'max_length': '1', 'editable': 'False', 'db_index': 'True'}),
            'status': ('models.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'wiki_link': ('models.URLField', [], {'blank': 'True'}),
            'youtube_link': ('models.URLField', [], {'blank': 'True'}),
            'zxdemo_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"ZXDemo ID"', 'blank': 'True'})
        },
        'webview.songplatform': {
            'Meta': {'ordering': "['title']"},
            'description': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/platform/image'", 'blank': 'True'}),
            'symbol': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/platform/symbol'", 'blank': 'True'}),
            'title': ('models.CharField', [], {'unique': 'True', 'max_length': '64'})
        },
        'webview.userprofile': {
            'aol_id': ('models.CharField', [], {'max_length': '40', 'verbose_name': '"AOL IM"', 'blank': 'True'}),
            'avatar': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/avatars'", 'blank': 'True'}),
            'country': ('models.CharField', [], {'max_length': '10', 'verbose_name': '"Country code"', 'blank': 'True'}),
            'custom_css': ('models.URLField', [], {'blank': 'True'}),
            'email_on_artist_add': ('models.BooleanField', [], {'default': 'True', 'verbose_name': '"Send email on artist approval"'}),
            'email_on_artist_comment': ('models.BooleanField', [], {'default': 'True', 'verbose_name': '"Send email on artist comments"'}),
            'email_on_group_add': ('models.BooleanField', [], {'default': 'True', 'verbose_name': '"Send email on group approval"'}),
            'email_on_pm': ('models.BooleanField', [], {'default': 'True', 'verbose_name': '"Send email on new PM"'}),
            'fave_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Fave SongID"', 'blank': 'True'}),
            'group': ('models.ForeignKey', ['Group'], {'null': 'True', 'blank': 'True'}),
            'hol_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"H.O.L. ID"', 'blank': 'True'}),
            'icq_id': ('models.CharField', [], {'max_length': '40', 'verbose_name': '"ICQ Number"', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'info': ('models.TextField', [], {'verbose_name': '"Profile Info"', 'blank': 'True'}),
            'infoline': ('models.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'last_active': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'last_activity': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'location': ('models.CharField', [], {'max_length': '40', 'verbose_name': '"Hometown Location"', 'blank': 'True'}),
            'paginate_favorites': ('models.BooleanField', [], {'default': 'True'}),
            'pm_accepted_upload': ('models.BooleanField', [], {'default': 'True', 'verbose_name': '"Send PM on accepted upload"'}),
            'real_name': ('models.CharField', [], {'max_length': '40', 'verbose_name': '"Real Name"', 'blank': 'True'}),
            'theme': ('models.ForeignKey', ['Theme'], {'null': 'True', 'blank': 'True'}),
            'token': ('models.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'twitter_id': ('models.CharField', [], {'max_length': '32', 'verbose_name': '"Twitter ID"', 'blank': 'True'}),
            'user': ('models.ForeignKey', ['User'], {'unique': 'True'}),
            'visible_to': ('models.CharField', [], {'default': '"A"', 'max_length': '1'}),
            'web_page': ('models.URLField', [], {'verbose_name': '"Website"', 'blank': 'True'}),
            'yahoo_id': ('models.CharField', [], {'max_length': '40', 'verbose_name': '"Yahoo! ID"', 'blank': 'True'})
        },
        'webview.ajaxevent': {
            'event': ('models.CharField', [], {'max_length': '100'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'user': ('models.ForeignKey', ['User'], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'webview.songdownload': {
            'Meta': {'ordering': "['title']"},
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'download_url': ('models.CharField', [], {'max_length': '200', 'unique': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'song': ('models.ForeignKey', ['Song'], {}),
            'title': ('models.CharField', [], {'max_length': '64'})
        },
        'webview.compilationvote': {
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'comp': ('models.ForeignKey', ['Compilation'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'user': ('models.ForeignKey', ['User'], {}),
            'vote': ('models.IntegerField', [], {'default': '0'})
        },
        'webview.uploadticket': {
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'filename': ('models.CharField', [], {'default': '""', 'max_length': '100', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'tempfile': ('models.CharField', [], {'default': '""', 'max_length': '100', 'blank': 'True'}),
            'ticket': ('models.CharField', [], {'max_length': '20'}),
            'user': ('models.ForeignKey', ['User'], {})
        },
        'webview.groupvote': {
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'group': ('models.ForeignKey', ['Group'], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'user': ('models.ForeignKey', ['User'], {}),
            'vote': ('models.IntegerField', [], {'default': '0'})
        },
        'webview.faq': {
            'Meta': {'ordering': "['priority']"},
            'active': ('models.BooleanField', [], {'default': 'True', 'verbose_name': '"Active?"', 'db_index': 'True'}),
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True'}),
            'added_by': ('models.ForeignKey', ['User'], {'null': 'True', 'blank': 'True'}),
            'answer': ('models.TextField', [], {'verbose_name': '"Answer"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'last_updated': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'}),
            'priority': ('models.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'question': ('models.CharField', [], {'max_length': '500', 'verbose_name': '"Question"'})
        },
        'webview.link': {
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True'}),
            'approved_by': ('models.ForeignKey', ['User'], {'related_name': '"label_approvedby"', 'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('models.CharField', [], {'verbose_name': '"Keywords"', 'max_length': '60', 'null': 'True', 'blank': 'True'}),
            'last_updated': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'}),
            'link_image': ('models.ImageField', [], {'verbose_name': '"Link Image"', 'null': 'True', 'upload_to': "'media/links/link_image'", 'blank': 'True'}),
            'link_title': ('models.CharField', [], {'max_length': '60', 'null': 'True', 'verbose_name': '"Link Desc."', 'blank': 'True'}),
            'link_type': ('models.CharField', [], {'default': "'T'", 'max_length': '1', 'verbose_name': '"Link Type"'}),
            'link_url': ('models.URLField', [], {'unique': 'True', 'verbose_name': '"Link URL"'}),
            'name': ('models.CharField', [], {'max_length': '40', 'unique': 'True', 'verbose_name': '"Link Name"'}),
            'notes': ('models.TextField', [], {'null': 'True', 'verbose_name': '"Link Notes"', 'blank': 'True'}),
            'priority': ('models.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'status': ('models.CharField', [], {'default': "'A'", 'max_length': '1', 'db_index': 'True'}),
            'submitted_by': ('models.ForeignKey', ['User'], {'related_name': '"label_submittedby"', 'null': 'True', 'blank': 'True'}),
            'url_cat': ('models.ForeignKey', ['LinkCategory'], {'verbose_name': '"Link Category"'})
        },
        'webview.artist': {
            'Meta': {'ordering': "['handle']"},
            'alias_of': ('models.ForeignKey', ["'self'"], {'related_name': "'aliases'", 'null': 'True', 'blank': 'True'}),
            'artist_pic': ('models.ImageField', [], {'upload_to': "'media/artists'", 'null': 'True', 'verbose_name': '"Picture"', 'blank': 'True'}),
            'created_by': ('models.ForeignKey', ['User'], {'related_name': '"artist_createdby"', 'null': 'True', 'blank': 'True'}),
            'deceased_date': ('models.DateField', [], {'null': 'True', 'verbose_name': '"Date Of Death"', 'blank': 'True'}),
            'dob': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'groups': ('models.ManyToManyField', ['Group'], {'null': 'True', 'blank': 'True'}),
            'handle': ('models.CharField', [], {'unique': 'True', 'max_length': '64', 'verbose_name': '"* Handle"', 'db_index': 'True'}),
            'hol_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"H.O.L. ID"', 'blank': 'True'}),
            'home_country': ('models.CharField', [], {'max_length': '10', 'verbose_name': '"Country Code"', 'blank': 'True'}),
            'home_location': ('models.CharField', [], {'max_length': '40', 'verbose_name': '"Location"', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'info': ('models.TextField', [], {'blank': 'True'}),
            'is_deceased': ('models.BooleanField', [], {'default': 'False', 'verbose_name': '"Deceased?"'}),
            'labels': ('models.ManyToManyField', ['Label'], {'null': 'True', 'blank': 'True'}),
            'last_fm_id': ('models.CharField', [], {'max_length': '32', 'verbose_name': '"Last.fm ID"', 'blank': 'True'}),
            'last_updated': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'}),
            'link_to_user': ('models.OneToOneField', ['User'], {'null': 'True', 'blank': 'True'}),
            'name': ('models.CharField', [], {'max_length': '64', 'verbose_name': '"Name"', 'blank': 'True'}),
            'startswith': ('models.CharField', [], {'max_length': '1', 'editable': 'False', 'db_index': 'True'}),
            'status': ('models.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'twitter_id': ('models.CharField', [], {'max_length': '32', 'verbose_name': '"Twitter ID"', 'blank': 'True'}),
            'webpage': ('models.URLField', [], {'verbose_name': '"Website"', 'blank': 'True'}),
            'wiki_link': ('models.URLField', [], {'blank': 'True'})
        },
        'webview.queue': {
            'eta': ('models.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'played': ('models.BooleanField', [], {'db_index': 'True'}),
            'playtime': ('models.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'}),
            'priority': ('models.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'requested': ('models.DateTimeField', [], {'auto_now_add': 'True', 'db_index': 'True'}),
            'requested_by': ('models.ForeignKey', ['User'], {}),
            'song': ('models.ForeignKey', ['Song'], {}),
            'time_played': ('models.DateTimeField', [], {'db_index': 'True', 'null': 'True', 'blank': 'True'})
        },
        'webview.linkcategory': {
            'Meta': {'ordering': "['name']"},
            'description': ('models.TextField', [], {'verbose_name': '"Description"'}),
            'icon': ('models.ImageField', [], {'verbose_name': '"Category Icon"', 'null': 'True', 'upload_to': "'media/links/slug_icon'", 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'id_slug': ('models.SlugField', ['_("Slug")'], {}),
            'name': ('models.CharField', [], {'max_length': '60', 'verbose_name': '"Category Name"'})
        },
        'webview.songcomment': {
            'Meta': {'ordering': "['-added']"},
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'comment': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'song': ('models.ForeignKey', ['Song'], {}),
            'user': ('models.ForeignKey', ['User'], {})
        },
        'webview.logo': {
            'active': ('models.BooleanField', [], {'default': 'True', 'db_index': 'True'}),
            'creator': ('models.CharField', [], {'max_length': '60'}),
            'description': ('models.TextField', [], {'blank': 'True'}),
            'file': ('models.FileField', [], {'upload_to': "'media/logos'"}),
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'webview.label': {
            'Meta': {'ordering': "['name']"},
            'cease_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'created_by': ('models.ForeignKey', ['User'], {'related_name': '"label_createdby"', 'null': 'True', 'blank': 'True'}),
            'found_date': ('models.DateField', [], {'null': 'True', 'blank': 'True'}),
            'hol_id': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"H.O.L. ID"', 'blank': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'info': ('models.TextField', [], {'blank': 'True'}),
            'label_icon': ('models.ImageField', [], {'verbose_name': '"Label Icon (Shows instead of default icon)"', 'null': 'True', 'upload_to': "'media/labels/icons'", 'blank': 'True'}),
            'last_updated': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'}),
            'logo': ('models.ImageField', [], {'verbose_name': '"Label Logo"', 'null': 'True', 'upload_to': "'media/labels'", 'blank': 'True'}),
            'name': ('models.CharField', [], {'unique': 'True', 'max_length': '40', 'verbose_name': '"* Name"', 'db_index': 'True'}),
            'pouetid': ('models.IntegerField', [], {'null': 'True', 'verbose_name': '"Pouet ID"', 'blank': 'True'}),
            'startswith': ('models.CharField', [], {'max_length': '1', 'editable': 'False', 'db_index': 'True'}),
            'status': ('models.CharField', [], {'default': "'A'", 'max_length': '1'}),
            'webpage': ('models.URLField', [], {'verbose_name': '"Website"', 'blank': 'True'}),
            'wiki_link': ('models.URLField', [], {'blank': 'True'})
        },
        'webview.favorite': {
            'Meta': {'ordering': "['song']", 'unique_together': '("user","song")'},
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'comment': ('models.TextField', [], {}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'song': ('models.ForeignKey', ['Song'], {}),
            'user': ('models.ForeignKey', ['User'], {})
        },
        'webview.songapprovals': {
            'approved': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'approved_by': ('models.ForeignKey', ['User'], {'related_name': '"uploadlist_approvedby"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'song': ('models.ForeignKey', ['Song'], {}),
            'uploaded_by': ('models.ForeignKey', ['User'], {'related_name': '"uploadlist_uploadedby"'})
        },
        'auth.user': {
            '_stub': True,
            'id': ('models.AutoField', [], {'primary_key': 'True'})
        },
        'webview.screenshot': {
            'active': ('models.BooleanField', [], {'default': 'True', 'verbose_name': '"Active?"', 'db_index': 'True'}),
            'added_by': ('models.ForeignKey', ['User'], {'related_name': '"screenshoit_addedby"', 'null': 'True', 'blank': 'True'}),
            'description': ('models.TextField', [], {'verbose_name': '"Description"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'image': ('models.ImageField', [], {'null': 'True', 'upload_to': "'media/screenshot/image'", 'blank': 'True'}),
            'last_updated': ('models.DateTimeField', [], {'null': 'True', 'editable': 'False', 'blank': 'True'}),
            'name': ('models.CharField', [], {'max_length': '70', 'unique': 'True', 'verbose_name': '"Screen Name"'}),
            'startswith': ('models.CharField', [], {'max_length': '1', 'editable': 'False', 'db_index': 'True'})
        },
        'webview.oneliner': {
            'Meta': {'ordering': "['-added']"},
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'message': ('models.CharField', [], {'max_length': '256'}),
            'user': ('models.ForeignKey', ['User'], {})
        },
        'webview.songvote': {
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'song': ('models.ForeignKey', ['Song'], {}),
            'user': ('models.ForeignKey', ['User'], {}),
            'vote': ('models.IntegerField', [], {})
        },
        'webview.artistvote': {
            'added': ('models.DateTimeField', [], {'auto_now_add': 'True'}),
            'artist': ('models.ForeignKey', ['Artist'], {}),
            'comment': ('models.CharField', [], {'max_length': '250', 'verbose_name': '"Comment"'}),
            'id': ('models.AutoField', [], {'primary_key': 'True'}),
            'rating': ('models.CharField', [], {'default': "'U'", 'max_length': '1'}),
            'user': ('models.ForeignKey', ['User'], {})
        }
    }
    
    complete_apps = ['webview']
