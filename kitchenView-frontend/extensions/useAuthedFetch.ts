const useAuthedFetch = async <T>(url: string, options: object = {}) => {
    const access_token = localStorage.getItem("access_token");
    return await $fetch<T>(url, {
        ...options,
        baseURL: useRuntimeConfig().public.baseURL,
        // @ts-ignore
        headers: access_token ? {"Authorization": `Bearer ${access_token}`, ...options.headers} : {...options.headers}
    });
};

export default useAuthedFetch