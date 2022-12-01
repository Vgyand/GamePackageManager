import React from 'react'
import ContentLoader from 'react-content-loader'

const SkeletonLoader = () => (
	<>
		<ContentLoader
			rtl
			speed={2}
			width={250}
			height={250}
			viewBox="0 0 250 250"
			backgroundColor="#5c284e"
			foregroundColor="#ecebeb"
		>
			<rect x="0" y="0" rx="3" ry="3" width="200" height="200" />
		</ContentLoader>
		<ContentLoader
			rtl
			speed={2}
			width={250}
			height={250}
			viewBox="0 0 250 250"
			backgroundColor="#5c284e"
			foregroundColor="#ecebeb"
		>
			<rect x="0" y="0" rx="3" ry="3" width="200" height="200" />
		</ContentLoader>
		<ContentLoader
			rtl
			speed={2}
			width={250}
			height={250}
			viewBox="0 0 250 250"
			backgroundColor="#5c284e"
			foregroundColor="#ecebeb"
		>
			<rect x="0" y="0" rx="3" ry="3" width="200" height="200" />
		</ContentLoader>
		<ContentLoader
			rtl
			speed={2}
			width={250}
			height={250}
			viewBox="0 0 250 250"
			backgroundColor="#5c284e"
			foregroundColor="#ecebeb"
		>
			<rect x="0" y="0" rx="3" ry="3" width="200" height="200" />
		</ContentLoader>
	</>
)

export default SkeletonLoader
