# -*- coding: utf-8 -*-

from openerp import api, fields, models


class Checklist(models.Model):
    _name = 'auditii.checklist'
    _description = 'Checklist'

    name = fields.Char('Name')
    result_ids = fields.Many2many('auditii.checklist.result.type', 'checklist_result_type_rel', 'checklist_id', 'result_id', 'Results')
    #requirement_ids = fields.One2many('auditii.checklist.requirement', 'checklist_id', 'Requirements')
    requirement_ids = fields.Many2many('auditii.checklist.requirement', 'auditii_checklist_requirement_rel', 'checklist_id', 'requeriment_id', 'Requeriments')
    template = fields.Boolean('Template', help='This checklist is a template')


class Requirement(models.Model):
    _name = 'auditii.checklist.requirement'
    _description = 'Requirement'

    checklist_id = fields.Many2one('auditii.checklist', 'Checklist')
    sequence = fields.Integer('Sequence')
    requirement = fields.Text('Requirement')
    observation = fields.Text('Observation')
    tip = fields.Text('Tip')
    tag_ids = fields.Many2many('auditii.checklist.requirement.tags', 'auditii_checklist_requirement_tag_rel', 'requirement_id', 'tag_id', 'Tags')
    result_id = fields.Many2one('auditii.checklist.result.type', 'Result', domain="[('checklist_ids', '=', checklist_id)]")


class ResultType(models.Model):
    _name = 'auditii.checklist.result.type'
    _description = 'Result Type'

    name = fields.Char('Name')
    sequence = fields.Integer('Sequence')
    checklist_ids = fields.Many2many('auditii.checklist', 'checklist_result_type_rel', 'result_id', 'checklist_id', 'Checklists')
    pts = fields.Integer('Points')


class RequirementTags(models.Model):
    _name = 'auditii.checklist.requirement.tags'
    _description = "Tags of checklist's requirements"

    name = fields.Char('Name')
    color = fields.Integer('Color Index')

    _sql_constraints = [
            ('name_uniq', 'unique (name)', "Tag name already exists !"),
    ]
