import pytest
from httpx import AsyncClient


async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post("/posts", json={"body": body})
    return response.json()


async def create_comment(body: str, post_id: int, async_client: AsyncClient) -> dict:
    response = await async_client.post(
        "/comments", json={"body": body, "post_id": post_id}
    )
    return response.json()


@pytest.fixture()
async def created_post(async_client: AsyncClient) -> dict:
    return await create_post("Post 1", async_client)


@pytest.fixture()
async def created_comment(async_client: AsyncClient, created_post: dict) -> dict:
    return await create_comment("Comment 1", created_post["id"], async_client)


@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    post_body = "Some Post"

    response = await async_client.post("/posts", json={"body": post_body})

    assert response.status_code == 201
    assert {"id": 1, "body": post_body}.items() <= response.json().items()


@pytest.mark.anyio
async def test_create_post_missing_data(async_client: AsyncClient):
    response = await async_client.post("/posts", json={})

    assert response.status_code == 422


@pytest.mark.anyio
async def test_get_all_posts(async_client: AsyncClient, created_post: dict):
    response = await async_client.get("/posts")

    assert response.status_code == 200
    assert created_post in response.json()
    assert response.json() == [created_post]


@pytest.mark.anyio
async def test_create_comment(async_client: AsyncClient, created_post: dict):
    comment_body = "A Comment"

    response = await async_client.post(
        "/comments", json={"body": comment_body, "post_id": created_post["id"]}
    )

    assert response.status_code == 201
    assert {
        "id": 1,
        "body": comment_body,
        "post_id": created_post["id"],
    }.items() <= response.json().items()


@pytest.mark.anyio
async def test_get_comments_on_post(
    async_client: AsyncClient, created_post: dict, created_comment: dict
):
    response = await async_client.get(f"/posts/{created_post['id']}/comments")

    assert response.status_code == 200
    assert created_comment in response.json()
    assert response.json() == [created_comment]


@pytest.mark.anyio
async def test_get_comments_when_no_comments(
    async_client: AsyncClient, created_post: dict
):
    response = await async_client.get(f"/posts/{created_post['id']}/comments")

    assert response.status_code == 200
    assert response.json() == []


@pytest.mark.anyio
async def test_get_post_with_comments(
    async_client: AsyncClient, created_post: dict, created_comment: dict
):
    response = await async_client.get(f"/posts/{created_post['id']}")

    assert response.status_code == 200
    assert response.json() == {
        "post": created_post,
        "comments": [created_comment],
    }


@pytest.mark.anyio
async def test_get_missing_post_with_comments(
    async_client: AsyncClient, created_post: dict, created_comment: dict
):
    response = await async_client.get(f"/posts/{created_post['id'] + 1}")

    assert response.status_code == 404
    assert response.json() == {"detail": "Post not found"}
