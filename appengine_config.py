from google.appengine.api.users import get_current_user

def namespace_manager_default_namespace_for_request():
    user = get_current_user()
    if user:
        return get_current_user().user_id()
    else:
        return None
