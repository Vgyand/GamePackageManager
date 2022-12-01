import { useGetMainPageQuery } from 'store/packsApi'

import Content from './Content/Content'

const ContentWrapper = () => {
	const { data } = useGetMainPageQuery('')
	console.log(data)
	return <Content />
}

export default ContentWrapper
