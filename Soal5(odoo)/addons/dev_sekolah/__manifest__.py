{
    'name': 'Dev Sekolah',
    'version': '1.0',
    'depends': ['base', 'web'],
    'application': True,  
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/sekolah_views.xml',
        'views/guru_views.xml',
        'views/menu.xml',  
        'views/kelas_views.xml',
        'views/inherit_sekolah_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'dev_sekolah/static/src/js/kelas_summary.js',
            'dev_sekolah/static/src/xml/kelas_summary.xml',
        ],
    },
    'application': True,
    'installable': True
}