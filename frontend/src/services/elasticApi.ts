import { createApi, fetchBaseQuery } from "@reduxjs/toolkit/query/react";


export const elasticApi = createApi({
  reducerPath: "elasticApi",
  baseQuery: fetchBaseQuery({
    baseUrl: "http://127.0.0.1:8000",
    prepareHeaders: (headers) => {
      const token = JSON.parse(localStorage.getItem('user') || '{}')?.access_token;
      if (token) {
        headers.set('Authorization', `Bearer ${token}`);
      }
      return headers;
    },
  }),
  endpoints: (builder) => ({
    getElasticData: builder.query<any, string>({
      query: () => ({
        url: `/elasticsearch/get_elastic_data`,
      })
    }),
    postElasticDataBySearch: builder.mutation<any, string>({
      query: (message) => ({
        url: `/elasticsearch/search`,
        method: "POST",
        body: {
          message: message
        }
      })
    }),
    postElasticDataBySearcWithDate: builder.mutation<any, {message: string, firstValue: any, secondValue: any}>({
      query: ({message, firstValue, secondValue}) => ({
        url: `/elasticsearch/search_by_date`,
        method: "POST",
        body: {
          message: message,
          begin: firstValue,
          end: secondValue
        }
      })
    }),
  }),
});

export const { usePostElasticDataBySearchMutation, usePostElasticDataBySearcWithDateMutation, useGetElasticDataQuery } = elasticApi;