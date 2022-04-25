PETEREPORT_CONFIG = {
	'admin_username': 'admin',
	'admin_password': 'P3t3r3p0rt',
	'admin_email': 'admin@petereport.pentest',
	'viewer_username': 'viewer',
	'viewer_password': 'v13w3r',
	'viewer_email': 'viewer@petereport.pentest'
}

DEFECTDOJO_CONFIG = {
	'DefectDojoURL': 'https://demo.defectdojo.org',
	'apiKey': 'Token Key' # Format: Token <api_key>
}

DJANGO_CONFIG = {
	'secret_key': 'django-insecure-key-CHANGEMEPLEASE-pKj9bd9h7*RMCuU',
	'debug': False,
	'admin_module': False,
	'allowed_hosts': '[\'*\']',
	'server_host': 'http://127.0.0.1:8000'
}

PETEREPORT_TEMPLATES = {
	'templates_root': 'preport/templates/tpl',
	'storage_reports': 'storage_reports',
	'html_template': 'bootstrap-4-pandoc-template/template.html',
	'pdf_latex_template': 'petereport.latex',
	'report_id_format': 'ASD-KMU-',
	'report_csv_name': 'PEN-CSV',
	'report_markdown_name': 'PEN-MD',
	'report_html_name': 'ASD-KMU-HTML',
	'report_pdf_name': 'ASD-KMU-PDF',
	'report_jupyter_name': 'PEN-JUPYTER',
	'initial_text': 'TBC',
	'titlepage-color': "FFFFFF",
	'titlepage-text-color': "D7322f",
	'titlepage-rule-color': "D7322f",
	'titlepage-rule-height': 2,
	'page-background': "asd.png"
}

PETEREPORT_MARKDOWN = {
	'author': 'Alter Solutions Deutschland',
	'subject': 'Ergebnisbericht IT-Sicherheitsanalyse KMU',
	'website': 'https://www.alter-solutions.de',
	'martor_upload_method': 'BASE64' # BASE64 (stored in DB) or MEDIA (path not protected)
}