# -*- coding: utf-8 -*-
# Unit 2 — My Family.  prefix U2, mascot Lily. 6 vocab (5 family + dog bonus).
UNIT = {
  'num': 2,
  'prefix': 'U2',
  'mascot_name': 'Lily',
  'journey_title': "Lily's Learning Journey",
  'hero_fallback': 'U2_IMG_001_Lily_Portrait.png',

  # ---------- SESSION 1 ----------
  's1_kicker_h1': ('My Family 👨‍👩‍👧‍👦','Learn <span class="pop">6 Words</span>','Listen 🔊 · Point 👈 · Say it 3 times',"Hi! I'm Lily 👧"),
  's1_sub': '5 family words + 1 bonus · say each 3 times',
  'vocab': [
    {'word':'family', 'img':'002_Lily_Family_Group',  'pcls':'f','phon':'/f/','grad':'#5AD3B0,#2FB089','vid':'U2_VID_002_Vocabulary_Family.mp4', 'aud':'U2_AUD_V01_Family.mp3'},
    {'word':'mother', 'img':'003_Rose_Mother_Portrait','pcls':'m','phon':'/m/','grad':'#FF8E7E,#FF5E48','vid':'U2_VID_002_Vocabulary_Mother.mp4', 'aud':'U2_AUD_V02_Mother.mp3'},
    {'word':'father', 'img':'004_Tom_Father_Portrait', 'pcls':'f','phon':'/f/','grad':'#B49BF5,#7A53E0','vid':'U2_VID_002_Vocabulary_Father.mp4', 'aud':'U2_AUD_V03_Father.mp3'},
    {'word':'sister', 'img':'005_Emma_Sister_Portrait','pcls':'s','phon':'/s/','grad':'#7DC0F5,#3E8BCF','vid':'U2_VID_002_Vocabulary_Sister.mp4', 'aud':'U2_AUD_V04_Sister.mp3'},
    {'word':'brother','img':'006_Max_Brother_Portrait','pcls':'b','phon':'/b/','grad':'#FFD86B,#FFB01E','vid':'U2_VID_002_Vocabulary_Brother.mp4','aud':'U2_AUD_V05_Brother.mp3'},
    {'word':'dog',    'img':'007_Milo_Dog_Portrait',  'pcls':'d','phon':'/d/','grad':'#5FE0BC,#2FB089','vid':'U2_VID_002_Vocabulary_Dog.mp4',    'aud':'U2_AUD_V06_Dog.mp3'},
  ],
  'preview': [('photo','📷','U2_AUD_HOOK_Story.mp3','#FF5E48'), ('name','🏷️','U2_AUD_013_Her_Name_Is_Rose.mp3','#43CFA6')],
  'say_word': 'brother',
  's1_tip': "🐾 <b>Lily's tip:</b> <b>/f/</b> — top teeth on lip, blow soft: family · father. <b>/m/</b> — lips together, hum: mother.",
  'match_words_order': ['brother','family','sister','mother','father','dog'],
  'match_pics_order':  ['mother','family','father','brother','sister','dog'],

  # ---------- SESSION 2 STORY (5 scenes) ----------
  'story': {
    'kicker_h1': ('Story Time 📖','Read with <span class="pop">Lily</span>','Watch · Read · Point to every word','Read with me! 📖'),
    'title':'My Family', 'cover_grad':'#FFE27A,#FFB01E',
    'full_aud':'U2_AUD_STORY_Full.mp3', 'video':'U2_VID_001_Story_My_Family.mp4',
    'scenes':[
      {'txt':'Lily has a photo.','img':'IMG_STORY_01_Lily_Photo','grad':'#FFE27A,#FFB01E','chip':'📷 photo','chipcol':'rgba(255,210,74,.25);color:#9A6B14'},
      {'txt':'This is my family.','img':'IMG_002_Lily_Family_Group','grad':'#5FE0BC,#2FB089','chip':'/f/ family','chipcol':'rgba(67,207,166,.18);color:#1F9874'},
      {'txt':'This is my mother. Her name is Rose.','img':'IMG_STORY_02_Mother_Rose','grad':'#FF9E8C,#FF5E48','chip':'/m/ mother','chipcol':'rgba(255,126,107,.15);color:#E0432C'},
      {'txt':'This is my father. His name is Tom.','img':'IMG_STORY_03_Father_Tom','grad':'#B49BF5,#7A53E0','chip':'/f/ father','chipcol':'rgba(155,123,240,.16);color:#7A53E0'},
      {'txt':'Milo is in my family too!','img':'IMG_007_Milo_Dog_Portrait','grad':'#7DC0F5,#3E8BCF','chip':'🐶 Milo','chipcol':'rgba(86,180,255,.16);color:#3E8BCF'},
    ],
  },

  # ---------- SESSION 3 GRAMMAR ----------
  'grammar': {
    'kicker_h1': ('Grammar Builder 🧩','my · her · <span class="pop">his</span>','Learn · Build · Check','Build with me! 🧩'),
    'video':'U2_VID_003_Grammar_My_Her_His.mp4', 'vlabel':'my / her / his',
    'aud':'U2_AUD_GRAMMAR_MyHerHis.mp3', 'title':'4 Magic Sentences', 'sub':'This is my · Her name is · His name is',
    'anchors':[['This','is','my','family.'],['This','is','my','mother.']],
    'legend':[('#16284A','who'),('#FF7E6B','is / name is'),('#43CFA6','my'),('#FFB01E','person')],
    'rounds':[
      {'tpl':['This','is','my','family.'],'say':'This is my family.'},
      {'tpl':['This','is','my','mother.'],'say':'This is my mother.'},
      {'tpl':['Her','name','is','Rose.'], 'say':'Her name is Rose.'},
      {'tpl':['His','name','is','Tom.'],  'say':'His name is Tom.'},
    ],
    'gestures':[('MY','touch your heart 🫶'),('HER','point to a girl 👧'),('HIS','point to a boy 👦'),('THIS IS','point to the photo 📷')],
    'parent':'Practice "my / her / his" with real family photos — point and say each person.',
    'tip':'⭐ <b>Key rule:</b> <b>my</b> = mine · <b>her</b> = girl · <b>his</b> = boy.',
  },

  # ---------- SESSION 4 PHONICS /f/ /m/ ----------
  'phonics': {
    'kicker_h1': ('Phonics 🔊','Two Sounds: <span class="pop">/f/ /m/</span>','/f/ air · /m/ hum','Try the sounds! 👄'),
    'sound1':{'letter':'Ff','ipa':'/f/','cue':'🦷 Top teeth on lip — blow soft!','aud':'U2_PHO_001_Sound_F.mp3','key':'f'},
    'sound2':{'letter':'Mm','ipa':'/m/','cue':'👄 Lips together — hum mmm!','aud':'U2_PHO_004_Sound_M.mp3','key':'m'},
    'video1':('U2_VID_004_Phonics_f_Sound.mp4','#FF9E8C,#FF5E48','/f/ — teeth on lip'),
    'video2':('U2_VID_004_Phonics_m_Sound.mp4','#5FE0BC,#2FB089','/m/ — hum'),
    'words1_title':'/f/ words',
    'words1':[('f','amily','U2_PHO_002_Word_Family.mp3'),('f','ather','U2_PHO_003_Word_Father.mp3'),('f','ish','U2_PHO_004_Word_Fish.mp3')],
    'words2_title':'/m/ words',
    'words2':[('m','other','U2_PHO_005_Word_Mother.mp3'),('m','at','U2_PHO_004_Sound_M.mp3'),('m','an','U2_PHO_004_Sound_M.mp3')],
    'pairs_sub':'/f/ vs /m/ — tap each one',
    'pairs':[('fan','U2_PHO_MIN_Fan.mp3','man','U2_PHO_MIN_Man.mp3'),
             ('fat','U2_PHO_MIN_Fat.mp3','mat','U2_PHO_MIN_Mat.mp3'),
             ('fine','U2_PHO_MIN_Fine.mp3','mine','U2_PHO_MIN_Mine.mp3')],
    'decode':['family','father','mother','man'],
    'parent':'Make the sounds face-to-face: /f/ blows soft air, /m/ hums with lips closed.',
    'tip':"🐾 <b>Lily's tip:</b> <b>/f/</b> is air, no voice. <b>/m/</b> hums — feel your lips buzz!",
  },

  # ---------- SESSION 5 SPEAKING ----------
  'speaking': {
    'kicker_h1': ('Speaking & Review ⭐','Tell Me About Your <span class="pop">Family</span>','Review · Record · Final','You did it! 🎉'),
    'title':'Tell me about your family! 🎙️',
    'levels':[
      ('🌱 Foundation · 10 sec','"This is my family. This is my mother."'),
      ('📘 Standard · 20 sec','"This is my family. This is my mother. Her name is Rose."'),
      ('⭐ Challenge · 30 sec','"This is my family. This is my mother. Her name is Rose. This is my father. His name is Tom. Milo is in my family too!"'),
    ],
    'video':('U2_VID_005_Speaking_Family_Model.mp4','#B49BF5,#7A53E0','Tell about your family'),
    'checklist':[
      'I can name 5 family words: family · mother · father · sister · brother (+ dog)',
      'I can read the family story with my finger',
      'I can say /f/ — teeth on lip: family · father',
      'I can say /m/ — hum: mother',
      'I can say 2–3 sentences about my family',
    ],
    'parent':'Let your child introduce family members (2-5 sentences) and record in the Moodle Speaking Activity.',
  },

  # ---------- COVER ----------
  'cover': {
    'kicker_h1': ('K1 English · Unit 2','My <span class="pop">Family</span>','Learn family words and sounds /f/ /m/',"Let's start! 👧"),
    'goals':[
      '🗣️ Say: <b>This is my family.</b>',
      '🗣️ Say: <b>This is my mother.</b>',
      '🗣️ Say: <b>Her name is Rose.</b>',
      '🦷 Make the <b>/f/</b> sound: family · father',
      '👄 Make the <b>/m/</b> sound: mother · Milo',
    ],
    'sessions':[
      ('1','Learn Words','5 family words'),
      ('2','Story Time',"Lily's family photo"),
      ('3','Grammar','my / her / his'),
      ('4','Phonics','Sounds /f/ /m/'),
      ('5','Speaking','Record + Final test'),
    ],
  },
}
