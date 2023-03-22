from django import template
# from django.conf import settings
from django.urls import reverse

register = template.Library()


@register.inclusion_tag('cms_dashboard/buttons/appraisal_listboard_button.html')
def appraisal_listboard_button(model_wrapper):
    title = ['Appraise employee.']
    url_name = "cms_dashboard:appraisal_listboard_url"
    redirect_url = reverse(url_name, kwargs={'contract': model_wrapper.id})
    return dict(
        href=redirect_url,
        contract=model_wrapper,
        title=' '.join(title))


@register.inclusion_tag('cms_dashboard/buttons/edit_appraisal_button.html')
def edit_appraisal_button(model_wrapper):
    title = ['Edit appraisal form.']
    return dict(
        # identifier=model_wrapper.object.identifier,
        href=model_wrapper.href,
        title=' '.join(title))


@register.inclusion_tag('cms_dashboard/buttons/edit_renewal_intent_button.html')
def edit_renewal_intent_button(model_wrapper):
    title = ['Edit renewal intent form.']
    return dict(
        # identifier=model_wrapper.object.identifier,
        href=model_wrapper.href,
        title=' '.join(title))


@register.inclusion_tag('cms_dashboard/buttons/edit_details_button.html')
def edit_details_button(model_wrapper):
    title = ['Edit details form.']
    return dict(
        identifier=model_wrapper.object.identifier,
        href=model_wrapper.href,
        title=' '.join(title))


@register.inclusion_tag('cms_dashboard/buttons/performance_imp_button.html')
def add_performance_imp_button(model_wrapper):
    title = ['Add performance improvement plan.']
    return dict(
        add_performance_imp=model_wrapper.href,
        title=' '.join(title))


@register.inclusion_tag('cms_dashboard/buttons/kpa_button.html')
def kpa_button(model_wrapper):
    return dict(
        add_kpa_href=model_wrapper.href,
        emp_identifier=model_wrapper.object.emp_identifier,
        kpa_object=model_wrapper.object)


@register.inclusion_tag('cms_dashboard/buttons/renewal_intent_button.html')
def renewal_intent_button(model_wrapper):
    return dict(
        add_renewal_intent_href=model_wrapper.href,
        emp_identifier=model_wrapper.object.emp_identifier,
        renewal_intent_object=model_wrapper.object)


@register.inclusion_tag('cms_dashboard/buttons/contracting_button.html')
def contracting_button(model_wrapper):
    return dict(
        add_contracting_href=model_wrapper.contracting.href,
        identifier=model_wrapper.contracting.identifier,
        contracting_model_obj=model_wrapper.contracting_model_obj
        # contracting_model_obj=model_wrapper.contract_model_obj
    )


@register.inclusion_tag('cms_dashboard/buttons/strategic_orientation_button.html')
def strategic_orientation_button(model_wrapper):
    wrapped_model_cls = model_wrapper.strategic_model_cls
    model_wrapper_cls = model_wrapper.strategic_wrapper_cls
    wrapped_model = model_wrapper.saved_or_unsaved_model(wrapped_model_cls,
                                                         model_wrapper_cls)
    return dict(
        add_strategic_orientation_href=wrapped_model.href,
        emp_identifier=model_wrapper.object.emp_identifier,
        strategic_orientation_obj=model_wrapper.strategic_model_obj)


@register.inclusion_tag('cms_dashboard/buttons/results_focus_button.html')
def results_focus_button(model_wrapper):
    wrapped_model_cls = model_wrapper.results_focus_model_cls
    model_wrapper_cls = model_wrapper.results_focus_wrapper_cls
    wrapped_model = model_wrapper.saved_or_unsaved_model(wrapped_model_cls,
                                                         model_wrapper_cls)
    return dict(
        add_results_focus_href=wrapped_model.href,
        emp_identifier=model_wrapper.object.emp_identifier,
        results_focus_obj=model_wrapper.results_focus_obj)


@register.inclusion_tag('cms_dashboard/buttons/leadership_and_motivation_button.html')
def leadership_and_motivation_button(model_wrapper):
    wrapped_model_cls = model_wrapper.leadership_model_cls
    model_wrapper_cls = model_wrapper.leadership_wrapper_cls
    wrapped_model = model_wrapper.saved_or_unsaved_model(wrapped_model_cls,
                                                         model_wrapper_cls)
    return dict(
        add_leadership_and_motivation_href=wrapped_model.href,
        emp_identifier=model_wrapper.object.emp_identifier,
        leadership_and_motivation_obj=model_wrapper.leadership_and_motivation_obj)


@register.inclusion_tag('cms_dashboard/buttons/innovation_and_creativity_button.html')
def innovation_and_creativity_button(model_wrapper):
    wrapped_model_cls = model_wrapper.innovation_model_cls
    model_wrapper_cls = model_wrapper.innovation_wrapper_cls
    wrapped_model = model_wrapper.saved_or_unsaved_model(wrapped_model_cls,
                                                         model_wrapper_cls)
    return dict(
        add_innovation_and_creativity_href=wrapped_model.href,
        emp_identifier=wrapped_model.object.emp_identifier,
        innovation_obj=model_wrapper.innovation_obj)


@register.inclusion_tag('cms_dashboard/buttons/planning_skills_button.html')
def planning_skills_button(model_wrapper):
    wrapped_model_cls = model_wrapper.planning_skills_model_cls
    model_wrapper_cls = model_wrapper.planning_skills_wrapper_cls
    wrapped_model = model_wrapper.saved_or_unsaved_model(wrapped_model_cls,
                                                         model_wrapper_cls)
    return dict(
        add_planning_skills_href=wrapped_model.href,
        emp_identifier=wrapped_model.object.emp_identifier,
        planning_skills_obj=model_wrapper.planning_skills_obj)


@register.inclusion_tag('cms_dashboard/buttons/interpersonal_skills_button.html')
def interpersonal_skills_button(model_wrapper):
    wrapped_model_cls = model_wrapper.interpersonal_skills_model_cls
    model_wrapper_cls = model_wrapper.interpersonal_skills_wrapper_cls
    wrapped_model = model_wrapper.saved_or_unsaved_model(wrapped_model_cls,
                                                         model_wrapper_cls)
    return dict(
        add_interpersonal_skills_href=wrapped_model.href,
        emp_identifier=wrapped_model.object.emp_identifier,
        interpersonal_obj=model_wrapper.interpersonal_obj)


@register.inclusion_tag('cms_dashboard/buttons/communication_skills_button.html')
def communication_skills_button(model_wrapper):
    wrapped_model_cls = model_wrapper.communication_skills_model_cls
    model_wrapper_cls = model_wrapper.communication_skills_wrapper_cls
    wrapped_model = model_wrapper.saved_or_unsaved_model(wrapped_model_cls,
                                                         model_wrapper_cls)
    return dict(
        add_communication_skills_href=wrapped_model.href,
        emp_identifier=wrapped_model.object.emp_identifier,
        communication_obj=model_wrapper.communication_obj)


@register.inclusion_tag('cms_dashboard/buttons/knowledge_and_productivity_button.html')
def knowledge_and_productivity_button(model_wrapper):
    wrapped_model_cls = model_wrapper.knowledge_model_cls
    model_wrapper_cls = model_wrapper.knowledge_wrapper_cls
    wrapped_model = model_wrapper.saved_or_unsaved_model(wrapped_model_cls,
                                                         model_wrapper_cls)
    return dict(
        add_knowledge_and_productivity_href=wrapped_model.href,
        emp_identifier=wrapped_model.object.emp_identifier,
        knowledge_obj=model_wrapper.knowledge_obj)


@register.inclusion_tag('cms_dashboard/buttons/quality_of_work_button.html')
def quality_of_work_button(model_wrapper):
    wrapped_model_cls = model_wrapper.quality_of_work_model_cls
    model_wrapper_cls = model_wrapper.quality_of_work_wrapper_cls
    wrapped_model = model_wrapper.saved_or_unsaved_model(wrapped_model_cls,
                                                         model_wrapper_cls)
    return dict(
        add_quality_of_work_href=wrapped_model.href,
        emp_identifier=wrapped_model.object.emp_identifier,
        quality_model_obj=model_wrapper.quality_model_obj)


@register.filter(name='professional_skills_btn')
def professional_skills_btn(skill_list_model):
    return f'{skill_list_model.short_name}_button'


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
