# Python Backend Exploration

This is a exploration repo for Python Backend projects with tutorials.

[![Github Pages](https://github.com/piyushpatel2005/django-exploration/actions/workflows/deploy.yml/badge.svg)](https://github.com/piyushpatel2005/django-exploration/actions/workflows/deploy.yml)

## Local Set up

- NodeJS 20.0 or above
- npm 7.0 or above

```bash
npm install
```

```bash
npm run dev
```


```bash
npm run build
```

```bash
npm run deploy
```

## Configurations

### Sidebar

The sidebar is generated using [starlight-sidebar-topics](https://starlight-sidebar-topics.netlify.app/docs/configuration/). You can change the order of items by passing `sidebar.order` in the frontmatter as shown in FastAPI pages.

## Adding New Lessons

- Create new directory structure like `src/content/docs/fastapi` for new tutorials on a topic.
- Add top level `title`, `prev` and `next` in each file. Also, include `order` to order the content in the sidebar.
- In the main `index.md` file, you might need to replace the links with `index.md` removed from there if you copied them from other exploration repos.

These files will be flattened in the Github action to make the sturcture like `src/content/docs/fastapi/topic.md` file structures.

## Adding to the Sidebar

- Modify the `astro.config.mjs` file to include the new directory in the sidebar to create custom sidebar for that topic tutorial.

Top level settings are in this file so if you want to change the title or the base url, you can modify here.

## Using splash template

If you're using `splash` template for any of the pages, you might need to define the `hero` object in the frontmatter of the file. If you're using that, you might need to change the `link` depending on your base url.

