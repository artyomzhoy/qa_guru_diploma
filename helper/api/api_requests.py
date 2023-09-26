from helper.api.custom_session import project_url


def get_account_base_info(username, headers):
    response = project_url.get(
        url=f'3/account/{username}',
        headers=headers
    )
    return response


def block_user(user, headers):
    response = project_url.post(
        url=f'account/v1/{user}/block',
        headers=headers
    )
    return response


def unblock_user(user, headers):
    response = project_url.delete(
        url=f'account/v1/{user}/block',
        headers=headers
    )
    return response


def get_block_list(headers):
    response = project_url.get(
        url='3/account/me/block',
        headers=headers
    )
    return response


def follow_tag(tag, headers):
    response = project_url.post(
        url=f'3/account/me/follow/tag/{tag}',
        headers=headers
    )
    return response


def unfollow_tag(tag, headers):
    response = project_url.delete(
        url=f'3/account/me/follow/tag/{tag}',
        headers=headers
    )
    return response


def get_tag_info(tag, headers):
    response = project_url.get(
        url=f'3/gallery/tag_info/{tag}',
        headers=headers
    )
    return response


def post_comment(headers, image_id, comment):
    response = project_url.post(
        url='3/comment',
        headers=headers,
        data={
            'image_id': f'{image_id}',
            'comment': f'{comment}'
        }
    )
    return response


def delete_comment(headers, comment_id):
    response = project_url.delete(
        url=f'3/comment/{comment_id}',
        headers=headers
    )
    return response


def get_comment(headers, comment_id):
    response = project_url.get(
        url=f'3/comment/{comment_id}',
        headers=headers
    )
    return response
