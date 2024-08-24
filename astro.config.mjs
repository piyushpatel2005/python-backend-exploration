import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// https://astro.build/config
export default defineConfig({
	site: 'https://piyushpatel2005.github.io',
	base: 'python-backend-exploration',
	integrations: [
		starlight({
			title: 'Python Dev',
			social: {
				github: 'https://github.com/piyushpatel2005/python-backend-exploration',
			},
			sidebar: [
				{
					label: 'Guides',
					items: [
						// Each item here is one entry in the navigation menu.
						{ label: 'Example Guide', slug: 'guides/example' },
					],
				},
				{
					label: 'Reference',
					autogenerate: { directory: 'reference' },
				},
				{
					label: 'Python',
					autogenerate: { directory: 'python' },
				},
				{
					label: 'Django',
					autogenerate: { directory: 'django' },
				},
				{
					label: 'FastAPI',
					autogenerate: { directory: 'fastapi' },
				}
			],
			components: {
				// Add custom components to the Astro project
				Sidebar: './src/overrides/Sidebar.astro',
			}
		}),
	],
});
