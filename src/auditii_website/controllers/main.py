# -*- coding: utf-8 -*-

import werkzeug
import openerp

from openerp import http
from openerp.http import request
from openerp.addons.web.controllers.main import Home


class Website(http.Controller):
    @http.route('/home', type='http', auth="none")
    def home(self, **kw):
        return request.render('auditii_website.layout')


class AdminWebsite(http.Controller):
    @http.route('/admin/contacts', type='http', methods=['GET'], auth="none")
    def get_contacts(self, **kw):
        contacts = request.env['res.partner'].sudo().search([])
        qcontext = {
            'contacts': contacts
        }
        return request.render('auditii_website.admin/contacts', qcontext)

    @http.route('/admin/contacts/<int:contact_id>', type='http', methods=['GET'], auth="none")
    def get_contact(self, contact_id, **kw):
        contact = request.env['res.partner'].sudo().search([('id','=',contact_id)])
        qcontext = {
            'contact': contact
        }
        return request.render('auditii_website.admin/contact', qcontext)

    @http.route(['/admin', '/admin/audits'], type='http', auth="none")
    def get_audits(self, **kw):
        audits = request.env['project.task'].sudo().search([])
        qcontext = {
            'audits': audits
        }
        return request.render('auditii_website.admin/audits', qcontext)

    @http.route('/admin/audits/<int:audit_id>', type='http', auth="none")
    def get_audit(self, audit_id, **kw):
        audit = request.env['project.task'].sudo().search([('id','=',audit_id)])
        qcontext = {
            'audit': audit
        }
        return request.render('auditii_website.admin/audit', qcontext)

    @http.route('/admin/audits/<int:audit_id>/assessment', type='http', auth="none")
    def audit_assessment(self, audit_id, **kw):
        return request.render('auditii_website.admin/audit/assessment')

    @http.route('/admin/complaints', type='http', auth="none")
    def complaints(self, **kw):
        return request.render('auditii_website.admin/complaints')

    @http.route('/admin/complaints/<int:complaint_id>', type='http', auth="none")
    def complaint(self, complaint_id, **kw):
        return request.render('auditii_website.admin/complaint')

    @http.route('/admin/reports/efficiency', type='http', auth="none")
    def reports_efficiency(self, **kw):
        return request.render('auditii_website.admin/reports/efficiency')

    @http.route('/admin/reports/complaints', type='http', auth="none")
    def reports_complaints(self, **kw):
        return request.render('auditii_website.admin/reports/complaints')

    @http.route('/admin/settings/tags/audits', type='http', auth="none")
    def get_settings_tags_audits(self, **kw):
        tags = request.env['project.tags'].sudo().search([])
        qcontext = {
            'tags': tags
        }
        return request.render('auditii_website.admin/settings/tags/audits', qcontext)

    @http.route('/admin/settings/tags/contacts', type='http', auth="none")
    def get_settings_tags_contacts(self, **kw):
        tags = request.env['res.partner.category'].sudo().search([])
        qcontext = {
            'tags': tags
        }
        return request.render('auditii_website.admin/settings/tags/contacts', qcontext)

    @http.route('/admin/settings/users', type='http', auth="none")
    def settings_users(self, **kw):
        users = request.env['res.users'].sudo().search([])
        qcontext = {
            'users': users
        }
        return request.render('auditii_website.admin/settings/users', qcontext)

    @http.route('/admin/settings/users/<int:user_id>', type='http', auth="none")
    def settings_user(self, user_id, **kw):
        user = request.env['res.users'].sudo().search([('id','=',user_id)])
        qcontext = {
            'user': user
        }
        return request.render('auditii_website.admin/settings/user', qcontext)

    @http.route('/admin/settings/integrations', type='http', auth="none")
    def settings_integrations(self, **kw):
        return request.render('auditii_website.admin/settings/integrations')
