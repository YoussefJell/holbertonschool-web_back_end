import {uploadPhoto, createUser} from './utils';

export default async function asyncUploadUser() {
	try {
		let [photo, user] = await Promise.all([uploadPhoto(), createUser()])
		return {
			photo: photo,
			user: user,
		  };
	} catch (err) {
		return {
			photo: null,
			user: null,
		  };
	}
}
