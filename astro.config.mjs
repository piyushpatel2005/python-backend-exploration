import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import starlightSidebarTopics from 'starlight-sidebar-topics';

// https://astro.build/config
const baseUrl = 'https://piyushpatel2005.github.io';
const base = baseUrl.endsWith('github.io') ? 'python-backend-exploration' : '';
export default defineConfig({
	site: baseUrl,
	base: base,
	integrations: [
		starlight({
			title: 'Python Explorations',
			customCss: [
				'./src/styles/custom.css'
			],
			social: [
				{ icon: 'github', label: 'GitHub', href: `https://github.com/piyushpatel2005/${base}` },
			],
			
			// Removed as no longer overriding but using starlight-sidebar-topics plugin
			components: {
				// Add custom components to the Astro project
				Sidebar: './src/overrides/Sidebar.astro',
				Topics: './src/overrides/Topics.astro',
			},
			plugins: [
				starlightSidebarTopics(
					[
						{
							label: 'Python',
							link: `/python/`,
							id: 'python',
							items: [{
								label: 'Python Tutorials',
								autogenerate: { directory: 'python/' },
							}]
						},
						{
							label: 'FastAPI',
							link: `/fastapi/`,
							id: 'fastapi',
							items: [{
								label: 'FastAPI Tutorials',
								autogenerate: { directory: 'fastapi/' },
							}]
						},
						{
							label: 'Django',
							link: `/django/`,
							id: 'django',
							items: [{
								label: 'Django Tutorials',
								autogenerate: { directory: 'django/' },
							}]
						},
					],
					{
						exclude: ['/guides/*', '/guides/**/*', '/reference/*', '/reference/**/*'],
					},
					{
						topics: {
							guides: ['guides/*', 'guides/**/*'],
							reference: ['reference/*', 'reference/**/*'],
						},
					}
				)
			]
		}),
	],
});
