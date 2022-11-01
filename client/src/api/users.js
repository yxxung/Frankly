import axios from 'axios'

// 로컬스토리지에서 access-token을 가지고 로그인.
function login(user, success, fail) {
    axios.defaults.headers["access-token"] = window.localStorage.getItem(
        "access-token"
    );
    const body = {
        email: user.userEmail,
        password: user.userPassword
    };

    axios.post('/api/auth/signin', JSON.stringify(body), {
        headers: {
            "Content-Type": `application/json`,
        },
    })
    .then(success)
    .catch(fail)
}

async function findByEmail(email, success, fail) {
    axios.defaults.headers["access-token"] = window.localStorage.getItem(
        "access-token"
    );
    await axios.get(`/api/users/${email}`)
        .then(success)
        .catch(fail)
}

export { login, findByEmail }