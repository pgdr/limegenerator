#!--
#!/usr/bin/env python
from __future__ import print_function

HEADER = """\
class	type/scale	name	relevance	text	help	language	validation	mandatory	other	default	same_default	allowed_filetypes	alphasort	answer_width	array_filter	array_filter_exclude	array_filter_style	assessment_value	category_separator	choice_title	code_filter	commented_checkbox	commented_checkbox_auto	cssclass	date_format	date_max	date_min	display_columns	display_rows	display_type	dropdown_dates	dropdown_dates_minute_step	dropdown_dates_month_style	dropdown_prefix	dropdown_prepostfix	dropdown_separators	dropdown_size	dualscale_headerA	dualscale_headerB	em_validation_q	em_validation_q_tip	em_validation_sq	em_validation_sq_tip	equals_num_value	equation	exclude_all_others	exclude_all_others_auto	hidden	hide_tip	input_boxes	label_input_columns	location_city	location_country	location_defaultcoordinates	location_mapheight	location_mapservice	location_mapwidth	location_mapzoom	location_nodefaultfromip	location_postal	location_state	max_answers	max_filesize	max_num_of_files	max_num_value	max_num_value_n	max_subquestions	maximum_chars	min_answers	min_num_of_files	min_num_value	min_num_value_n	multiflexible_checkbox	multiflexible_max	multiflexible_min	multiflexible_step	num_value_int_only	numbers_only	other_comment_mandatory	other_numbers_only	other_replace_text	page_break	parent_order	prefix	printable_help	public_statistics	random_group	random_order	rank_title	repeat_headings	reverse	samechoiceheight	samelistheight	scale_export	show_comment	show_grand_total	show_title	show_totals	showpopups	slider_accuracy	slider_custom_handle	slider_default	slider_handle	slider_layout	slider_max	slider_middlestart	slider_min	slider_orientation	slider_rating	slider_reset	slider_separator	slider_showminmax	statistics_graphtype	statistics_showgraph	statistics_showmap	suffix	text_input_columns	text_input_width	time_limit	time_limit_action	time_limit_countdown_message	time_limit_disable_next	time_limit_disable_prev	time_limit_message	time_limit_message_delay	time_limit_message_style	time_limit_timer_style	time_limit_warning	time_limit_warning_2	time_limit_warning_2_display_time	time_limit_warning_2_message	time_limit_warning_2_style	time_limit_warning_display_time	time_limit_warning_message	time_limit_warning_style	use_dropdown	value_range_allows_missing
S		sid		333472																																																																																																																																					
S		owner_id		1																																																																																																																																					
S		admin		Administrator																																																																																																																																					
S		active		N																																																																																																																																					
S		adminemail		{_EMAIL}																																																																																																																																					
S		anonymized		N																																																																																																																																					
S		format		G																																																																																																																																					
S		savetimings		N																																																																																																																																					
S		template																																																																																																																																							
S		language		en																																																																																																																																					
S		datestamp		N																																																																																																																																					
S		usecookie		N																																																																																																																																					
S		allowregister		N																																																																																																																																					
S		allowsave		Y																																																																																																																																					
S		autonumber_start		0																																																																																																																																					
S		autoredirect		N																																																																																																																																					
S		allowprev		N																																																																																																																																					
S		printanswers		N																																																																																																																																					
S		ipaddr		N																																																																																																																																					
S		refurl		N																																																																																																																																					
S		datecreated		2018-10-02																																																																																																																																					
S		publicstatistics		N																																																																																																																																					
S		publicgraphs		N																																																																																																																																					
S		listpublic		N																																																																																																																																					
S		htmlemail		Y																																																																																																																																					
S		sendconfirmation		Y																																																																																																																																					
S		tokenanswerspersistence		N																																																																																																																																					
S		assessments		N																																																																																																																																					
S		usecaptcha		N																																																																																																																																					
S		usetokens		N																																																																																																																																					
S		bounce_email		{_EMAIL}																																																																																																																																					
S		tokenlength		15																																																																																																																																					
S		showxquestions		Y																																																																																																																																					
S		showgroupinfo		B																																																																																																																																					
S		shownoanswer		N																																																																																																																																					
S		showqnumcode		X																																																																																																																																					
S		bounceprocessing		N																																																																																																																																					
S		showwelcome		Y																																																																																																																																					
S		showprogress		Y																																																																																																																																					
S		questionindex		0																																																																																																																																					
S		navigationdelay		0																																																																																																																																					
S		nokeyboard		N																																																																																																																																					
S		alloweditaftercompletion		N																																																																																																																																					
SL		surveyls_title		{_SURVEY_TITLE}		en																																																																																																																																			
SL		surveyls_email_invite_subj		Invitation to participate in a survey		en																																																																																																																																			
SL		surveyls_email_invite		"Dear {{FIRSTNAME}},<br /> <br /> you have been invited to participate in a survey.<br /> <br /> The survey is titled:<br /> ""{{SURVEYNAME}}""<br /> <br /> ""{{SURVEYDESCRIPTION}}""<br /> <br /> To participate, please click on the link below.<br /> <br /> Sincerely,<br /> <br /> {{ADMINNAME}} ({{ADMINEMAIL}})<br /> <br /> ----------------------------------------------<br /> Click here to do the survey:<br /> {{SURVEYURL}}<br /> <br /> If you do not want to participate in this survey and don't want to receive any more invitations please click the following link:<br /> {{OPTOUTURL}}<br /> <br /> If you are blacklisted but want to participate in this survey and want to receive invitations please click the following link:<br /> {{OPTINURL}}"		en																																																																																																																																			
SL		surveyls_email_remind_subj		Reminder to participate in a survey		en																																																																																																																																			
SL		surveyls_email_remind		"Dear {{FIRSTNAME}},<br /> <br /> Recently we invited you to participate in a survey.<br /> <br /> We note that you have not yet completed the survey, and wish to remind you that the survey is still available should you wish to take part.<br /> <br /> The survey is titled:<br /> ""{{SURVEYNAME}}""<br /> <br /> ""{{SURVEYDESCRIPTION}}""<br /> <br /> To participate, please click on the link below.<br /> <br /> Sincerely,<br /> <br /> {{ADMINNAME}} ({{ADMINEMAIL}})<br /> <br /> ----------------------------------------------<br /> Click here to do the survey:<br /> {{SURVEYURL}}<br /> <br /> If you do not want to participate in this survey and don't want to receive any more invitations please click the following link:<br /> {{OPTOUTURL}}"		en																																																																																																																																			
SL		surveyls_email_register_subj		Survey registration confirmation		en																																																																																																																																			
SL		surveyls_email_register		Dear {{FIRSTNAME}},<br /> <br /> You, or someone using your email address, have registered to participate in an online survey titled {{SURVEYNAME}}.<br /> <br /> To complete this survey, click on the following URL:<br /> <br /> {{SURVEYURL}}<br /> <br /> If you have any questions about this survey, or if you did not register to participate and believe this email is in error, please contact {{ADMINNAME}} at {{ADMINEMAIL}}.		en																																																																																																																																			
SL		surveyls_email_confirm_subj		Confirmation of your participation in our survey		en																																																																																																																																			
SL		surveyls_email_confirm		Dear {{FIRSTNAME}},<br /> <br /> this email is to confirm that you have completed the survey titled {{SURVEYNAME}} and your response has been saved. Thank you for participating.<br /> <br /> If you have any further questions about this email, please contact {{ADMINNAME}} on {{ADMINEMAIL}}.<br /> <br /> Sincerely,<br /> <br /> {{ADMINNAME}}		en																																																																																																																																			
SL		surveyls_dateformat		6		en																																																																																																																																			
SL		email_admin_notification_subj		Response submission for survey {{SURVEYNAME}}		en																																																																																																																																			
SL		email_admin_notification		Hello,<br /> <br /> A new response was submitted for your survey '{{SURVEYNAME}}'.<br /> <br /> Click the following link to reload the survey:<br /> {{RELOADURL}}<br /> <br /> Click the following link to see the individual response:<br /> {{VIEWRESPONSEURL}}<br /> <br /> Click the following link to edit the individual response:<br /> {{EDITRESPONSEURL}}<br /> <br /> View statistics by clicking here:<br /> {{STATISTICSURL}}		en																																																																																																																																			
SL		email_admin_responses_subj		Response submission for survey {{SURVEYNAME}} with results		en																																																																																																																																			
SL		email_admin_responses		Hello,<br /> <br /> A new response was submitted for your survey '{{SURVEYNAME}}'.<br /> <br /> Click the following link to reload the survey:<br /> {{RELOADURL}}<br /> <br /> Click the following link to see the individual response:<br /> {{VIEWRESPONSEURL}}<br /> <br /> Click the following link to edit the individual response:<br /> {{EDITRESPONSEURL}}<br /> <br /> View statistics by clicking here:<br /> {{STATISTICSURL}}<br /> <br /> <br /> The following answers were given by the participant:<br /> {{ANSWERTABLE}}		en																																																																																																																																			
SL		surveyls_numberformat		0		en																																																																																																																																			
""".format(_EMAIL='insert@email.here',
           _SURVEY_TITLE='Insert Survey Title Here')

# notice that in the above, the double braces {{ X }} is so that they
# aren't formatted with .format (which would raise error on missing key)

MAXLEN = 17

TAIL = ',,en,,,N,,1,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,1'

DAY = 'G,G{id_},Group {id_},1,,,en,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,'
DAYCOUNTER = 0

prevday = None

def slugify(s, postfix=None):
    if postfix is None:
        postfix = ''
    slug = ''.join(x for x in s if x.isalnum()).lower()
    if len(slug) > MAXLEN:
        slug = slug[:MAXLEN]
    return slug + postfix

def q(type_, key, sectionid, title):
    return ('Q,{type_},{key},{sectionid},"{title}"'.format(
        type_=type_,
        key=key,
        sectionid=sectionid,
        title=title) + TAIL).replace(',', '\t')


def question(section, types, the_question):
    global prevday, DAYCOUNTER
    q1, q2 = '', ''
    if '5' in types:
        q1 = q('5', slugify(section+the_question), 1, the_question)
    if 'T' in types:
        q2 = q('T', slugify(section+the_question, postfix='txt'), 1, 'Comments to ' + the_question)
    if section != prevday:
        q1 = DAY.replace(',', '\t').format(id_=DAYCOUNTER) + '\n' + q1
        DAYCOUNTER += 1
        prevday = section
    return q1 + '\n' + q2

def main(fname):
    with open(fname, 'r') as f:
        data = f.readlines()

    print(HEADER)

    for l in data:
        line = l.strip()
        if line:
            print(question(*line.split(',')))


if __name__ == '__main__':
    from sys import argv
    if len(argv) < 2:
        exit('Usage: python limegenerator.py survey.csv > survey.txt')
    main(argv[1])
