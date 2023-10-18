import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";

export const authApi = createApi({
  reducerPath: "authApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000",
  }),
  endpoints: (builder) => ({
    loginUser: builder.mutation({
      query: (formData: FormData) => {
        formData.append("grant_type", "");
        formData.append("scope", "");
        formData.append("client_id", "");
        formData.append("client_secret", "");

        const body = new URLSearchParams();
        formData.forEach((value, key) => {
          body.append(key, value.toString());
        });

        return {
          url: "/auth/login",
          method: "post",
          body: body.toString(),
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      }
    }),
    registerUser: builder.mutation({
      query: (body: {
        email: string,
        name: string,
        password: string,
        role_id: 0
      }) => {
        return {
          url: "/auth/register",
          method: "post",
          body,
        }
      }
    }),
  }),
});

export const { useLoginUserMutation, useRegisterUserMutation } = authApi;