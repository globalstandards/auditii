# -*- coding: utf-8 -*-

from openerp import api, fields, models, _


class Project(models.Model):
    _inherit = 'project.project'

    aii_audit_project = fields.Boolean('Audit Project')


class AuditTask(models.Model):
    _inherit = 'project.task'

    aii_checklist_tpl_id = fields.Many2one('auditii.checklist', 'Checklist template', domain=[('template', '=', True)])
    aii_assessment_id = fields.Many2one('auditii.checklist', 'Assessment', domain=[('template', '=', False)])

    @api.model
    def create(self, vals):
        res = super(AuditTask, self).create(vals)
        res._create_assessment()
        return res

    def _create_assessment(self):
        if not self.project_id or not self.project_id.aii_audit_project:
            return

        assessment = self.aii_checklist_tpl_id.copy({
            'template': False
        })
        self.write({
            'aii_assessment_id': assessment.id
        })

    @api.multi
    def action_open_assessment(self):
        self.ensure_one()
        return {
            'name': _('Assessments'),
            'res_model': 'auditii.checklist',
            'type': 'ir.actions.act_window',
            'view_id': self.env.ref('auditii.assessment_view_form').id,
            'view_mode': 'form',
            'res_id': self.aii_assessment_id.id
        }
