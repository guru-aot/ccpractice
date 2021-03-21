export interface RequestState {
  requestHeaders: [];
  requestList: RequestModel[];
  loading?: boolean;
  successStatus?: boolean;
  errorStatus?: boolean;
}
export interface RequestModel {
  name: string;
  description: string;
  requestid: string;
  status: string;
  createdby: string;
  created_at: string;
  updated_at: string;
  updated: string;
}
