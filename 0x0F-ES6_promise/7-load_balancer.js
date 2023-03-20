export default async function loadBalancer(chinaDownload, USDownload) {
	return await Promise.race([chinaDownload, USDownload]);
}
